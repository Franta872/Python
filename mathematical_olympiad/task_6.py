# osmiboký jehlan s devíti čísly
import time

cisla = []
for cislo in range(11, 30): # 11 – 29
    if not cislo % 4 == 0:
        cisla.append(cislo)

print(cisla)
jonas = 0
michal = 0
celkem = 0
start = time.perf_counter()
for Po in cisla:
    for Tr1 in cisla:
        for Tr2 in cisla:
            for Tr3 in cisla:
                for Tr4 in cisla:
                    for Tr5 in cisla:
                        for Tr6 in cisla:
                            for Tr7 in cisla:
                                for Tr8 in cisla:
                                    if len([Po, Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8]) != len(set([Po, Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8])):
                                        continue # kontrola toho, jestli tam nejsou stejné čísla
                                    if (Po + Tr1 + Tr2) % 4 != 0:
                                        continue # Mohl bych tady všude naspat "and", ale aby to nekontrolovalo
                                                 # všechno, tak stačí zjistit že jedna podmínka neplatí a jde to dál.
                                    if (Po + Tr2 + Tr3) % 4 != 0:
                                        continue
                                    if (Po + Tr3 + Tr4) % 4 != 0:
                                        continue
                                    if (Po + Tr4 + Tr5) % 4 != 0:
                                        continue
                                    if (Po + Tr5 + Tr6) % 4 != 0:
                                        continue
                                    if (Po + Tr6 + Tr7) % 4 != 0:
                                        continue
                                    if (Po + Tr7 + Tr8) % 4 != 0:
                                        continue
                                    if (Po + Tr1 + Tr8) % 4 != 0:
                                        continue
                                    if (Tr1 + Tr2 + Tr3 + Tr4 + Tr5 + Tr6 + Tr7 + Tr8) % 4 != 0:
                                        continue
                                    print(Po, Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8)
                                    celkem += 1
                                    if [Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8].count(14) >= 1 and [Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8].count(15) >= 1:
                                        print("Jonáš")
                                        jonas += 1
                                    if [Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8].count(14) >= 1 and [Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8].count(17) >= 1:
                                        print("Michal")
                                        michal += 1
print(f"Jonáš: {jonas}")
print(f"Michal: {michal}")
print(f"Celkem: {celkem}")
print(f"Čas: {time.perf_counter() - start} s")
input()