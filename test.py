# test
import constyle as cs
import random
import os
import time
import difflib
import string

class animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

class Dog(animal):
    def speaking(self):
        print("WOOF!")

dog = Dog("Miša")

print(dog.is_alive)