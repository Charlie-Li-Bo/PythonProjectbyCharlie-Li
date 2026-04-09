"""
File: Steeplechase.py
Name: 李昀柏
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
     # Karel面向東
        if front_is_clear():
            move()
        else:
            jump()
    # Karel面向南



def jump():
    rise()
    drop()

def rise():
    """
    Pre:Karel面向東
    Post:Karel面向北
    """
    turn_left()
    while not right_is_clear():
        # Karel面向東
        move()
        # Karel面向北
    turn_right()
    move()
    turn_right()

def drop():
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()








# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
