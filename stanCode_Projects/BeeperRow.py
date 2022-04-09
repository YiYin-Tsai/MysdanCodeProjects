"""
File: BeeperRow.py
Name:Lisa
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    while front_is_clear():
        put_beeper()
        while front_is_clear():
            move()
            put_beeper()
        turn_left()








"""
while front_is_clear():
->重複
if front_is_clear():
->單次
"""















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)