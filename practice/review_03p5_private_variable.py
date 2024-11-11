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

# ==========================
# REVIEW - PRIVATE VARIABLES
# ==========================

# 1. MAKE A VARIABLE PRIVATE
'''
Do the same as the previous, but make DogPerson's `dog_list` variable private.
Add a method to DogPerson called `add_dog` that will append a dog to the 
`dog_list` variable. Add some dog objects to a DogPerson object and then run
`introduce_yourself` and print out the result.
'''

class Person: 
    def __init__(self, name, hobby): 
        self.name = name 
        self.hobby = hobby 

    def introduce_yourself(self):
        return f"Hello, my name is {self.name} and my hobby is {self.hobby}"

class DogPerson(Person):
    def __init__(self, name, hobby):
        super().__init__(name, hobby)
        self.dog_list = []

    def introduce_yourself(self):
        message = super().introduce_yourself()
        if self.dog_list:
            message += f" and these are my dogs:\n"
            for dog in self.dog_list:
                message += f"\t{dog.dog_info()}\n"
        else:
            message += f" but I don't have a dog yet!"
        return message

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def dog_info(self):
        return f"{self.name}, {self.breed}"


dog_1 = Dog("Max", "Golden Retriever")
dog_2 = Dog("James", "Husky")
dog_3 = Dog("Alice", "Poodle")

dog_person = DogPerson("Jimmy", "Basketball")
dog_person_2 = DogPerson("Samantha", "Tennis")

print(dog_person.introduce_yourself())
print(dog_person_2.introduce_yourself())