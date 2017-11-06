import os
from termcolor import cprint, colored
from bcolors import bcolors
import time


class board:
    arri = [3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 36]
    arrj = [1, 2, 3, 4, 9, 10, 11, 12, 17, 18, 19, 20, 25, 26, 27, 28, 33, 34,
            35, 36, 41, 42, 43, 44, 49, 50, 51, 52, 57, 58, 59, 60, 65, 66, 67,
            68, 73, 74,
            75, 76]

    def make_board(self):
        ret = {}
        for i in range(1, self.__h + 1):
            for j in range(1, self.__w + 1):
                if i <= 2 or i >= self.__h - 1:
                    ret[i, j] = "*"
                elif i not in self.arri and j in self.arrj:
                    ret[i, j] = "*"
                elif j <= 4 or j >= self.__w - 3:
                    ret[i, j] = "*"
                else:
                    ret[i, j] = " "
        return ret

    def __init__(self, height, width):
        self.__h = height
        self.__w = width

    def show(self, ret, user, immortal):
        for i in range(1, self.__h + 1):
            for j in range(1, self.__w + 1):
                if (i <= 2 or i >= self.__h - 1) and ret[i, j] == " ":
                    ret[i, j] = "*"
                elif ((i not in self.arri and j in self.arrj) and
                        ret[i, j] == " "):
                    ret[i, j] = "*"
                elif (j <= 4 or j >= self.__w - 3) and ret[i, j] == " ":
                    ret[i, j] = "*"
                print(ret[i, j], end='')
            print()

    def colored_show(self, ret, user, immortal):
        if immortal:
            n = user[4]._x
            m = user[4]._y
            for i in range(n, n + 2):
                for j in range(m, m + 4):
                    ret[i, j] = "B"
        for i in range(1, self.__h + 1):
            for j in range(1, self.__w + 1):
                # If bomb explodes in the wall then this is required ####
                if (i <= 2 or i >= self.__h - 1) and ret[i, j] == " ":
                    ret[i, j] = "*"
                elif ((i not in self.arri and j in self.arrj) and
                        ret[i, j] == " "):
                    ret[i, j] = "*"
                elif (j <= 4 or j >= self.__w - 3) and ret[i, j] == " ":
                    ret[i, j] = "*"
#############################################
                if ret[i, j] == 'E':
                    print(bcolors.FAIL + 'E' + bcolors.ENDC, end='')
                elif ret[i, j] == "*":
                    print(bcolors.OKGREEN + '*' + bcolors.ENDC, end='')
                elif ret[i, j] == "B":
                    if user[4]._super_power is None:
                        print(bcolors.OKBLUE + "B" + bcolors.ENDC, end='')
                    elif user[4]._super_power is not None:
                        print(colored("B", 'white', attrs=['bold']),
                              end='')

                elif ret[i, j] == '/':
                    print(bcolors.HEADER + '/' + bcolors.ENDC, end='')
                else:
                    print(bcolors.WARNING + ret[i, j] + bcolors.ENDC, end='')
            print()

if __name__ == "__main__":
    a = board(38, 76)
    z = a.make_board()
