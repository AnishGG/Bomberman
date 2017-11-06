import sys
from termcolor import colored, cprint
from powerup import powerup
from bcolors import bcolors
from inp import *
from board import board
from bomberman import bomberman
from bomb import bomb
from unoccupied import unoccupied
from enemy import enemy
from brick import brick


def speed(time_count, how_much):
    if how_much == 'normal':
        time.sleep(0.1)
        time_count += 0.1
        time_count = round(time_count, 1)
    elif how_much == 'twice':
        time.sleep(0.05)
        time_count += 0.05
        time_count = round(time_count, 2)
    return time_count


# index will tell how many enemies to move
def enemy_mover(ene, user, count, un, oc, immortal):
    enemy_count = 0
    for i in ene:
        if count <= 0:
            if i.give_status():
                enemy_count += 1
        elif i.give_status():
            enemy_count += 1
            i.random_move(immortal)
        count -= 1
    if enemy_count == 0:
        user[3] = 1


def resume():
    while True:
        print("Resume: y/n")
        char = input()
        if char in ("y", "n"):
            break
    return char


def print_board(a, a_a, user, immortal, time_counter):
    a.colored_show(a_a, user, immortal)
    print(bcolors.BOLD + "Score: " + bcolors.ENDC,
          user[0], bcolors.BOLD + "   Lives: " + bcolors.ENDC, user[1],
          bcolors.BOLD + "   Time Left: " + bcolors.ENDC, time_counter)
    b = user[4]._super_power
    if b is not None:
        print(bcolors.BOLD + "Super Power: " + bcolors.ENDC, end="")
    if b == "S":
        print(bcolors.BOLD + "SPEED ENHANCED" + bcolors.ENDC)
    elif b == "L":
        print(bcolors.BOLD + "LARGE EXPLOSION" + bcolors.ENDC)
    elif b == "I":
        print(bcolors.BOLD + "IMMORTALITY" + bcolors.ENDC)
    elif b == "W":
        print(bcolors.BOLD + "WALL PASS" + bcolors.ENDC)
    if time_counter <= 0:
        print(bcolors.BOLD + "Sorry, TIME UP" + bcolors.ENDC)


def won(user):
    print(bcolors.UNDERLINE +
          "CONGRATULATION YOU KILLED ALL THE ENEMIES" + bcolors.ENDC)
    print()


def power_ticker(b):
    if b._powerup is not None:
        b._powerup.tick()


def every_moment(b, a_a, a, immortal):
    char = get_char_keyboard_nonblock()
    if char in ("q", "p", "a", "w", "s", "d", "b"):
        if char is "a":
            b.move_left(immortal)
        elif char is "w":
            b.move_up(immortal)
        elif char is "d":
            b.move_right(immortal)
        elif char is "s":
            b.move_down(immortal)
        elif char is "p":
            if b._powerup is None or b._powerup.status():
                if b._super_power is None:
                    b._powerup = powerup(b)
        elif char is "q":
            sys.exit()
        else:
            b.drop_bomb()
# user array contains score, lives, zinda hai?, whether user won, (x-y coords)

if __name__ == "__main__":
    user = []
    user.append(0)  # Score
    user.append(3)  # number of lives
    user.append(1)  # zinda hai?
    user.append(0)  # won or not
    user.append(bomberman(3, 5, board(38, 76).make_board(), [], [], 'normal'))
    while user[1] != 0 and user[3] == 0:
        enemy_count = 0
        got_inside_block = False
        a = board(38, 76)
        a_a = a.make_board()    # This will have dictionary
        x = unoccupied()
        un = x._un
        oc = x._oc
        ene = []
        fast_ene = []
        bricks = []
        time_count = 0.0
        for i in range(1, 6):
            ene.append(enemy(un, oc, a_a, user))
        for i in range(1, 20):
            bricks.append(brick(un, oc, a_a))
        b = bomberman(3, 5, a_a, user, ene, 'normal')
        b._wallpass = False
        immortal = False
        # This problem in implementation, pass bomberman in bomb to avoid it
        user[4] = b
        new_speed = 'normal'
        bomb_effect = 'normal'
        power_up_timer = 0
        time_counter = 120
###############################################################################
        while user[2] == 1 and user[3] == 0 and time_counter > 0:
            time_count = speed(time_count, new_speed)
    # GIVING POWERUP #############
            if b._super_power == "S":
                new_speed = 'twice'
            elif b._super_power == "L":
                b._bomb_effect = 'large'
            elif b._super_power == "I":
                immortal = True
            elif b._super_power == "W":
                b._wallpass = True
    ########################################
            if time_count.is_integer():
                time_counter -= 1
                b._bom.tick(immortal)
                if b._super_power is not None:
                    # As power_up is only to be given for 10 seconds
                    power_up_timer += 1
    # TAKING ALL POWERS BACK ###########
                if power_up_timer > 10:
                    power_up_timer = 0
                    new_speed = 'normal'
                    b._bomb_effect = 'normal'
                    immortal = False
                    b._wallpass = False
                    b._super_power = None
    ###############################################
            every_moment(b, a_a, a, immortal)  # function call
            fast_count = 2
            slow_count = 5
            os.system('cls' if os.name == 'nt' else 'clear')
            if (time_count.is_integer() is False and
                    (2 * time_count).is_integer()):
                enemy_mover(ene, user, fast_count, un, oc, immortal)
            if time_count.is_integer():
                power_ticker(b)
                enemy_mover(ene, user, slow_count, un, oc, immortal)
            if user[2] == 0 or user[3] == 1:
                break
            print_board(a, a_a, user, immortal, time_counter)
# 33
        if user[3] == 1:
            break
        b.dead()
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(a, a_a, user, immortal, time_counter)
        user[1] -= 1  # decreasing life
        user[2] = 1  # zinda again man
        char = resume()
        if char not in ("y", "Y"):
            break
    os.system('cls' if os.name == 'nt' else 'clear')
    print_board(a, a_a, user, immortal, time_counter)
    if user[3] == 1:
        won(user)
