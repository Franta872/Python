# 2 písemky a jejich hodnocení

#            |  1. písemka | 2. písemka
# celá třída |      84     |      70
# 4 žáci     |      63     |      63
# bez 4 žáků |      ??     |      72

ctiri_zaci = [63]*4 # čtyři žáci vyjádření jejich hodnocením
ostatni = [72] # počet ostatních žáků vyjádřený jejich hodnocením
#            [63]*4  [70]*(1 až 14)   [63]*4  [70]*(1 až 14)  
while not sum(ctiri_zaci+ostatni)/len(ctiri_zaci+ostatni) == 70:
    ostatni.append(72)
print(f"Celkem žáků: {len(ostatni)}+4")
#       Celkem žáků:       14      +4

body_ostatnich_zaku = 1
#                [63]*4     body od 1 do 90         14          14 + 4 = 18
while not sum(ctiri_zaci+[body_ostatnich_zaku]*len(ostatni))/(len(ostatni)+4) == 84:
    body_ostatnich_zaku += 1
print(f"Průměr třídy bez 4 žáků v 1. písemce: {body_ostatnich_zaku} b.")

# Odpověď: Celkem je 14+4 žáků a ostatní žáci mají
#          v druhé písemce průměr 90 bodů.