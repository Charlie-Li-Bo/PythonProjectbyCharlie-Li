"""
File: MoveToTheEnd.py
Name:李昀柏
------------------------
This program demonstrates how to use a
while loop to move Karel to the end of
a row in the Karel world.

By checking whether the front is clear,
Karel will keep moving forward until it
reaches the end of the row.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will move to the end of the first Street in any world
    """
    pass
    move_7()

def move_7():
    for i in range(7):
        move()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
