# Bomberman:

### Usage:
* This game requires python3 or greater, and all the modules are given in requirements.txt
* These modules are to be installed be following command:
* pip install -r requirements.txt
* Fully tested in "konsole"(open source terminal-emulator)
* To install konsole ->  sudo apt-get install konsole

The game would start in terminal(konsole) by executing the following command:
* python3 main.py

### Controls:
    move-left  -> a
    move-right -> d
    move-up    -> w
    move-down  -> s
    drop-bomb  -> b
    power-up   -> p
    quit-game  -> q
 
### Powerups:
* Four types of power ups are provided: speed increase, bomb power increase, immortality, wall pass.
 1. speed increase is represented by "S"
 2. bomb power increase is represented by "L"
 3. immortality is represented by "I"
 4. wall pass is represented by "W"

### More INFO:
* Enemies are of two types: One type moves with normal speed(1 move per 1 second) and the other with double speed.
* As of now only 1 level is implemented which includes 6 enemies fixed and 3 lives for bomberman and 20 bricks.
* killing one enemy gives 100 points and destroying a brick gives 20 points.

