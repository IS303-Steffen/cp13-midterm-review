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

# ====================
# REVIEW - INHERITANCE
# ====================

# 1. MAKE A NEW CLASS THAT INHERITS FROM THE PARENT

'''
I'm giving you starting code for the Person.
Make a DogPerson class that inherits from Person.
    - They have the same instance variables, but DogPerson also has a variable
      called dog, for a string to store a dog name.
    - Use super() to call the Person constructor.
    - The method introduce_yourself should be overridden so that it also says
    "and my dog's name is <dog>" after the original string.

Make a Person object, then a DogPerson object. call introduce_yourself() on 
both.
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

# make a person and a dogperson.
person = Person("Jim", "Basketball")
dog_person = DogPerson("Jenny", "Cycling", "Max")

# run introduce_yourself() on each of the objects.
print(person.introduce_yourself())
print(dog_person.introduce_yourself())
