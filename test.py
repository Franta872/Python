# test
import constyle as cs
import random
import os
import time
import difflib
import string

def wild(sym:list, emoji:str, wild="⭐"):
    if ([emoji]*2+[wild] == sym) or ([emoji, wild, emoji] == sym) or ([wild]+[emoji]*2 == sym):
        return True
    else:
        return False

def check(sym):
    winning = 0
    if sym == ["💎"]*3 or wild(sym, "💎"):
        winning = 100
    elif sym == ["🔔"]*3 or wild(sym, "🔔"):
        winning = 25
    elif sym == ["🍉"]*3 or wild(sym, "🍉"):
        winning = 15
    elif sym == ["🍋"]*3 or wild(sym, "🍋"):
        winning = 10
    elif sym == ["🍒"]*3 or wild(sym, "🍒"):
        winning = 5
    elif wild(sym, "⭐", "💎") or wild(sym, "⭐", "🔔") or wild(sym, "⭐", "🍉") or wild(sym, "⭐", "🍋") or wild(sym, "⭐", "🍒"):
        winning = 3
    elif sym == ["⭐"]*3:
        winning = "bonus"

    print(winning)
check(["⭐"]*3)