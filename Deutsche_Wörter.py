import random
import time
import difflib
import constyle as cs

vocabulary = {
    "ne": ("nein"),
    "ano": ("ja"),
    "a": ("und"),
    "já": ("ich"),
    "ty": ("du"),
    "on": ("er"),
    "ona": ("sie"),
    "ono": ("es"),
    "my": ("wir"),
    "vy": ("ihr"),
    "oni": ("sie"),
    "Vy": ("Sie")
}

cz, nj = random.choice(list(vocabulary.items()))

if random.randint(0, 1) == 1:
    print("němčina: ", nj)
    answer = input("český překlad: ")
else:
    print("čeština", cz)
    answer = input("německý překlad: ")