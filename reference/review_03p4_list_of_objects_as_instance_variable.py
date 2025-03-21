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
# REVIEW - AGGREGATION 2: PUTTING OBJECTS IN DATA STRUCTURES
# ==========================================================

# 1. PUT OBJECTS IN AN INSTANCE VARIABLE LIST
'''
Do the same as the previous, but now DogPerson's `dog` variable should be
`dog_list`, which should initially be an empty list.

Alter Dog to include a method called `dog_info`.
    - it should return "name, breed"

Alter DogPerson's introduce_yourself. If they have at least one dog, say:
    "Hello, my name is <name> and my hobby is <hobby> and these are my dogs:"
        then run `dog_info` on each of their dogs.
        It should return a string with the first sentence and all the `dog_info`
        sentences.
    
    But if they have no dogs, return :
    "Hello, my name is <name> and my hobby is <hobby> but I don't have a dog yet!"

Make a DogPerson, and add 3 dogs to their list.
Make another DogPerson, but don't add any dogs to their list.
run introduce_yourself on both andn print the result.
'''

class Person: # name of the class
    def __init__(self, name, hobby): # self MUST come first, then any other parameters you want to pass in
        self.name = name # instance variable
        self.hobby = hobby # instance variable

    def introduce_yourself(self): # method. Self MUST be a parameter
        return f"Hello, my name is {self.name} and my hobby is {self.hobby}" # get to the instance parameters by referencing self.

# make your DogPerson class here
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

#add three dogs to dog_person's list:
dog_person.dog_list.append(dog_1)
dog_person.dog_list.append(dog_2)
dog_person.dog_list.append(dog_3)

print(dog_person.introduce_yourself())
print(dog_person_2.introduce_yourself())