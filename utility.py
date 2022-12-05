# utility.py
# A module with various useful functions by Omer Golan-Joel
# v3.1 - July 19th, 2020
# This is open source code, feel free to use it for any purpose
# contact me at golan2072@gmail.com

# import modules
import random
import os
import platform

# functions


def dice(n, sides):
    die = 0
    roll = 0
    while die < n:
        roll = roll + random.randint(1, sides)
        die += 1
    return roll


def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')