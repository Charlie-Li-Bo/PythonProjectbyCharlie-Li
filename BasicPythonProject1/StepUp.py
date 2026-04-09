"""
File: StepUp.py
Name: 李昀柏
------------------------
This program demonstrates how Karel picks up a beeper
at Street 1 Avenue 2 and moves it to Street 2 Avenue 4.

By guiding Karel step by step, we will practice writing
clear and well-structured commands. At the end of the
program, Karel will be facing East at Street 2 Avenue 5.
"""

from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    move()
    pick_beeper()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    turn_left()
    move()
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    put_50()
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    move()
    put_50()
    turn_right()
    turn_right()


def put_50():
    for i in range(50):
        put_beeper()










# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
