import random
import time
import constyle.constyle as cs

credits = 100
winnings = ["🍒", "🍋", "🍉", "🔔", "⭐", "💎"]
winning = 0
last_free = False

def game():
    waiting = 0
    symbols_before = random.choices(winnings, weights=[5, 4, 3, 2, 2, 1], k=3)
    symbols = random.choices(winnings, weights=[5, 4, 3, 2, 2, 1], k=3)
    symbols_after = random.choices(winnings, weights=[5, 4, 3, 2, 2, 1], k=3)
    while True:
        symbols_after = symbols.copy()
        symbols = symbols_before.copy()
        symbols_before = random.choices(winnings, weights=[5, 4, 3, 2, 2, 1], k=3)
        print("*"*40)
        print(f'{"  |  ".join(symbols_before):^40}')
        print(f'{"--->"+"  |  ".join(symbols)+"<---":^40}')
        print(f'{"  |  ".join(symbols_after):^40}')
        print("*"*40)
        time.sleep(waiting)
        if waiting < 0.48:
            cs.clear("line", 5)
            waiting += 0.02
            continue
        else:
            break
    return symbols

def wild(sym:list, emoji:str, wild="⭐"):
    if sym.count(emoji) == 2 and sym.count(wild) == 1:
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
    if winning == "bonus":
        sentence = random.choice(("Toto i přístí kolo máš zdarma!", "Teď i příště hraješ zadara!", "Toto kolo je zdarma a dokonce i to příští"))
    elif winning > 0:
        sentence = random.choice((f"Počet vyhraných kreditů je {winning}", f"Tobě to ale jde, toto je počet vyhraných kreditů: {winning}"))
    elif winning == 0:
        sentence = random.choice(("Příšte to určitě vyjde.", "Nentokrát to nevyšlo.", "Zkus to ještě jednou, to určitě vyjde."))
    print(sentence, end="\n\n")

    input("\nZmáčkněte Enter pro přesun do menu: ")
    cs.clear("line", 10)
    return winning

while True:
    print("*"*40)
    print(cs.bold(f'{"VÝHERNÍ AUTOMAT":^40}'))
    print("*"*40)
    print(f"Váš kredit: {cs.bold(credits)}")
    if last_free:
        print("Další hru máte zdarma")
    else:
        print("Cena hry je " + cs.bold("1 kredit"))
    print()
    print("Pro hru stiskněte Enter")
    print(cs.italic("Pro exit zadejte exit"))

    if input().strip().lower() in ("ne", "n", "no", "exit", "leave", "odejít"):
        exit()
    else:
        cs.clear("line", 9)
        winning = check(game())
        if not last_free:
            credits -= 1
        if last_free:
            last_free = False
        if winning == "bonus":
            last_free = True
        elif winning > 0:
            credits += winning
        continue