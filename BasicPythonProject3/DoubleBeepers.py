"""
File: DoubleBeepers.py
Name:李昀柏
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    pick_5()
    move()
    put_10()
    turn_left()
    turn_left()
    pick_10()
    move()
    put_20()
    move()
    turn_left()
    turn_left()



def pick_5():
    for i in range(5):
        pick_beeper()

def put_10():
    for i in range(10):
        put_beeper()

def put_20():
    for i in range(20):
        put_beeper()

def pick_10():
    for i in range(10):
        pick_beeper()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
