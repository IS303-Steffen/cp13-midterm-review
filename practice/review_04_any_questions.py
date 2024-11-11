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

# =======================
# REVIEW - ANY QUESTIONS?
# =======================

'''
If there are any individual questions that you'd like me to cover, I will
go over them here.
'''