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

class Person: # name of the class
    def __init__(self, name, hobby): # self MUST come first, then any other parameters you want to pass in
        self.name = name # instance variable
        self.hobby = hobby # instance variable

    def introduce_yourself(self): # method. Self MUST be a parameter
        return f"Hello, my name is {self.name} and my hobby is {self.hobby}" # get to the instance parameters by referencing self.


person1 = Person("Jim", "Basketball")
person2 = Person("Jenny", "Cycling")

print(person1.introduce_yourself())
