import random
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
total = 0

while True:
    dices = input("How many dice do you want to roll? ")
    if not dices.isdigit():
        print("It must be a number!")
        continue
    dices = int(dices)
    if dices < 1:
        print("The number must be higher than zero!")
        continue
    break
dices_numbers = list(random.randint(1, 6) for x in range(dices))
for x in dices_numbers:
    total += x

for x in range(len(dice_art[1])):
    for y in dices_numbers:
        print(dice_art[y][x], end="")
    print()
print(f"Total is: {total}")