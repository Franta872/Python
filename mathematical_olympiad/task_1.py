# 3 prvočísla

prvocisla = [2]

for x in range(3, 194):
    if not x % 2 == 0:
        je_prvocislo = True
        for y in prvocisla:
            if x % y == 0:
                je_prvocislo = False
                break
        if je_prvocislo:
            prvocisla.append(x)


for p1 in prvocisla:
    for p2 in prvocisla:
        for p3 in prvocisla:
            if (p2 - p1) * (p3 - p1) == 195:
                print(f"({p2} - {p1}) * ({p3} - {p1}) = 195")


# odpověď:
#         (5 - 2) * (67 - 2) = 195
#         p2   p1    p3   p1
#
#         (5 - 2) * (67 - 2) = 195
#         p2   p1    p3   p1
#
# Pak by to šlo ještě kdyby jsme ty závorky prohodily, 
# takže jsou vlastně 4 odpovědi.