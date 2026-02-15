# test
#import constyle as cs
#import random
#import os
#import time
#import difflib
#import string
#import itertools
#import math
#import unicodedata

def sirup(func):
    def wrapper(*args, **kwargs):
        print("sirup added")
        func(*args, **kwargs)
    return wrapper
def sprinkles(func):
    def wrapper(*args, **kwargs):
        print("sprinkles added")
        func(*args, **kwargs)
    return wrapper

@sprinkles
@sirup
def ice_cream(flavour):
    print(flavour, "ice cream (:")

ice_cream("vanilla")