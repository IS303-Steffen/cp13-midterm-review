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

# ==========================================================
# REVIEW - AGGREGATION (PUTTING AN OBJECT IN ANOTHER OBJECT)
# ==========================================================

# 1. MAKE A NEW CLASS, MAKE AN OBJECT, AND PUT IT IN ANOTHER OBJECT
'''
Do the same as the previous, but make a Dog class
    - Instance variables: Name, Breed
    - methods:
        - __init__() (the constructor)

Now, instead of a DogPerson's dog variable holding a string, make it hold a Dog
object.

Alter DogPerson's introduce_yourself to say:
"Hello, my name is <name> and my hobby is <hobby> and my <breed>'s name is
<dog name>."

Make a Dog
Make a DogPerson, and then run introduce_yourself on that DogPerson and print
out the result.
'''

class Person: # name of the class
    def __init__(self, name, hobby):
        self.name = name # instance variable
        self.hobby = hobby # instance variable

    def introduce_yourself(self): # method. 
        return f"Hello, my name is {self.name} and my hobby is {self.hobby}"


# make your DogPerson class here
class DogPerson(Person):
    def __init__(self, name, hobby, dog):
        super().__init__(name, hobby)
        self.dog = dog

    def introduce_yourself(self):
        message = super().introduce_yourself()
        return message + f" and my dog's name is {self.dog}"

