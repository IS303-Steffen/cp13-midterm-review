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

# 1. PUT OBJECTS IN LISTS AND RUN METHODS ON THEM
'''
You are given a Person and 2 DogPerson objects. Put them all into a list,
loop through the list and print out the result of their `introduce_yourself`
method.

Make sure that when a Person object runs `introduce_yourself`, it does the 
Person version and when a DogPerson object runs it, it does their customized
version.
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
        self.__dog_list = []

    def introduce_yourself(self):
        message = super().introduce_yourself()
        if self.__dog_list:
            message += f" and these are my dogs:\n"
            for dog in self.__dog_list:
                message += f"\t{dog.dog_info()}\n"
        else:
            message += f" but I don't have a dog yet!"
        return message
    
    def add_dog(self, dog):
        self.__dog_list.append(dog)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def dog_info(self):
        return f"{self.name}, {self.breed}"

dog_1 = Dog("Max", "Golden Retriever")
dog_2 = Dog("James", "Husky")
dog_3 = Dog("Alice", "Poodle")

person = Person("George", "Politics")
dog_person = DogPerson("Jimmy", "Basketball")
dog_person_2 = DogPerson("Samantha", "Tennis")

dog_person.add_dog(dog_3)
dog_person_2.add_dog(dog_1)
dog_person_2.add_dog(dog_2)
person_list = [person, dog_person, dog_person_2]

# please note that lowercase person is different than Person!!!
for person in person_list: 
    print(person.introduce_yourself())
