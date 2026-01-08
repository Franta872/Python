# test
import constyle as cs
import random
import os
import time
import difflib

answer = "ahoj"
test = ["ahoj", "Ahoj"]

print(max(map(lambda x: difflib.SequenceMatcher(None, answer.lower(), x).ratio(), test)))