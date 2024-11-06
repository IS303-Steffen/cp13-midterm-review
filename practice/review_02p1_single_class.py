import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ===============================
# REVIEW - SINGLE CLASS & OBJECTS
# ===============================

# 1. MAKE A CLASS AND OBJECTS
'''
make a Person class
    Instance variables: name, hobby

    Methods:
        __init__ (the constructor)
        introduce_yourself
            return "Hello, my name is <name> and my hobby is <hobby>"

Make two Person objects. run the introduce_yourself method on both of them
and print the result
'''

