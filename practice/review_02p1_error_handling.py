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

# ==================================
# REVIEW - HANDLING INVALID INPUT
# ==================================

# 1.1 ERROR HANDLING - DEFENSIVE CODING STYLE
# Given the code below, make it so it will continually
# ask for a new input until a valid one is given.
# Do NOT use try/except.

example_dict = {"Jimmy": 35, "Hannah": 47, "Bobby": 16}
name_input = input("Enter a name to see their age: ")
print(example_dict[name_input])



# 1.2 ERROR HANDLING - EXCEPTION HANDLING
# Given the code below, make it so it will continually
# ask for a new input until a valid one is given.
# You MUST use try/except. Uncomment the code to start out.

# example_dict = {"Jimmy": 35, "Hannah": 47, "Bobby": 16}
# name_input = input("Enter a name to see their age: ")
# print(example_dict[name_input])
