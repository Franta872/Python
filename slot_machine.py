import random
import time
import constyle.constyle as cs

credits = 100
winnings = ["🍒", "🍋", "🍉", "🔔", "⭐", "💎"]

def menu(bonus=None):
    global credits
    print("*"*40)
    print(cs.bold(f'{"VÝHERNÍ AUTOMAT":^40}'))
    print("*"*40)
    print(f"Váš kredit: {cs.bold(credits)}")
    if bonus == "bonus":
        print("Další hru máte zdarma\n")
        credits += 1
    else:
        print()
    print("Pro hru stiskněte Enter")
    print(cs.italic("Pro exit zadejte exit"))

    if input().strip().lower() in ("ne", "n", "no", "exit", "leave", "odejít"):
        exit()
    else:
        cs.clear("line", 9 if bonus == "bonus" else 8)
        game()

def game():
    waiting = 0
    while True:
        symbols = random.choices(winnings, weights=[5, 4, 3, 2, 2, 1], k=3)
        print("*"*40)
        print(f'{symbols[0]+"  |  "+symbols[1]+"  |  "+symbols[2]:^40}')
        print("*"*40)
        time.sleep(waiting)
        if waiting < 0.48:
            cs.clear("line", 3)
            waiting += 0.02
            continue
        else:
            break
    check(symbols)

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
    global credits
    if winning == "bonus":
        print("Tuto a další hru máš zdarma")
    elif winning <= 0:
        print("Prohrál jsi")
        credits -= 1
    else:
        credits = (credits-1)+winning
        print(f"Počet vyhraných kreditů: {cs.bold(winning)}")
    input("\nZmáčkněte Enter pro přesun do menu: ")
    cs.clear("line", 6)
    menu(winning)

menu()