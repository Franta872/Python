# test
import constyle as cs
import random
import os
import time
import difflib
import string
import itertools
import math
import unicodedata

splitText = "tentoTextBudeRozdělenPoDvouAsiDoufám"
print(len(splitText))
range_int = 2
for y in [(x, x+range_int) for x in range(0, len(splitText)//range_int*range_int, range_int)]:
    print(splitText[y[0]:y[1]], end=" ")