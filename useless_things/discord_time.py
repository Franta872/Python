# funguje pouze ve středoevropském letním čase!!!

from datetime import datetime

neededItems = {"year": range(1970, 10000),
               "month": range(1, 13),
               "day": range(1, 32),
               "hour": range(0, 24),
               "minute": range(0, 60),
               "second": range(0, 60)}
items = dict()
while True:
    try:
        for item in neededItems.keys():
            while True:
                x = input(f"Enter {item} in number in range {min(neededItems[item])}–{max(neededItems[item])}: ")
                if not x.isdigit():
                    print(f"{x} is not a valid number!")
                    continue
                elif not int(x) in neededItems[item]:
                    print(f"{x} is not in range! ({min(neededItems[item])}–{max(neededItems[item])})")
                    continue
                else:
                    items.update({item: int(x)})
                    break
        datetime(*items.values())
        break
    except ValueError:
        print("Month is out of range!")
        continue

types = ("F", "d", "t", "R")
found = False
while not found:
    typeOfMessage = input("Enter type: F=whole date, d=only date, t=only time, R=relative time (best): ").strip()
    for type in types:
        if typeOfMessage.lower() == type.lower():
            output = f'Message: <t:{int((datetime(*items.values()) - datetime(1970, 1, 1, 2, 0, 0)).total_seconds())}:{type}>'
            found = True
            break
    else:
        print(f"{typeOfMessage} is invalid!")
        continue

print(output)

# <t:1775059200:R>   1. dubna 2026 18:00

