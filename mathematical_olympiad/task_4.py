# 2 písemky

#            |  1. písemka | 2. písemka
# celá třída |      84     |      70
# 4 žáci     |      63     |      63
# bez 4 žáků |      ??     |      72

ctiri_zaci = [63]*4
ostatni = [72]
while True:
    if sum(ctiri_zaci+ostatni)/len(ctiri_zaci+ostatni) == 70:
        print(f"Celkem žáků: {len(ostatni)}+4")
        break
    else:
        ostatni.append(72)
# Celkem žáků: 14+4

body_ostatnich_zaku = 1
while True:
    if sum(ctiri_zaci+[body_ostatnich_zaku]*14)/(len(ostatni)+4) == 84:
        print(f"Průměr třídy bez 4 žáků v 1. písemce: {body_ostatnich_zaku} b.")
        break
    else:
        body_ostatnich_zaku += 1

# Odpověď: Celkem je 14+4 žáků a ostatní žáci mají
#          v druhé písemce průměr 90 bodů.