#animovaný obdelík nebo čtverec
import constyle as cs
import time

while True:
    delka = input("Jaká bude délka? ").strip()
    if not delka.isdigit():
        print("Délka musí být číslo")
        continue
    elif delka == "0":
        print("Délka nesmí být 0")
        continue
    else:
        delka = int(delka)
        break
while True:
    vyska = input("Jaká bude výška? ")
    if not vyska.isdigit():
        print("Výška musí být číslo")
        continue
    elif vyska == "0":
        print("Výška nesmí být 0")
        continue
    else:
        vyska = int(vyska)
        break
vyska_anim = 1
delka_anim = 1
for x in range(max(vyska, delka)):
    cs.clear("line", vyska_anim)
    delka_text = ""
    delka_iter = round(delka_anim*2.1) # to tam je protože ─ je asi 2.1krát ktatší než │
    for x in range(delka_iter-2):
        delka_text += "─"
    print("╭"+delka_text+"╮", flush=True)
    for x in range(vyska_anim-2):
        print("│", end="", flush=True)
        for y in range(delka_iter-2):
            print(" ", end="", flush=True)
        print("│", flush=True)
    print("╰"+delka_text+"╯", flush=True)

    if delka_anim != delka:
        delka_anim += 1
    if vyska_anim != vyska:
        vyska_anim += 1
    time.sleep(0.2)

input() # kdyby to někdo spustil jako program a ne z terminálu, tak by se mu to hned zavřelo. Tohle tomu zamezuje.