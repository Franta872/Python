# osmiboký jehlan s devíti čísly


cisla = []
for cislo in range(11, 30): # 11 – 29
    if not cislo % 4 == 0:
        cisla.append(cislo)

print(cisla)
jonas = 0
michal = 0
for Po in cisla:
    for Tr1 in  cisla:
        for Tr2 in cisla:
            for Tr3 in cisla:
                for Tr4 in cisla:
                    for Tr5 in cisla:
                        for Tr6 in cisla:
                            for Tr7 in cisla:
                                for Tr8 in cisla:
                                    if len([Po, Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8]) != len(set([Po, Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8])):
                                        continue
                                    if (Po + Tr1 + Tr2) % 4 == 0 and \
                                    (Po + Tr2 + Tr3) % 4 == 0 and \
                                    (Po + Tr3 + Tr4) % 4 == 0 and \
                                    (Po + Tr4 + Tr5) % 4 == 0 and \
                                    (Po + Tr5 + Tr6) % 4 == 0 and \
                                    (Po + Tr6 + Tr7) % 4 == 0 and \
                                    (Po + Tr7 + Tr8) % 4 == 0 and \
                                    (Po + Tr1 + Tr8) % 4 == 0 and \
                                    (Tr1 + Tr2 + Tr3 + Tr4 + Tr5 + Tr6 + Tr7 + Tr8) % 4 == 0:
                                        print(Po, Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8)
                                        if [Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8].count(14) >= 1 and [Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8].count(15) >= 1:
                                            print("Jonáš")
                                            jonas += 1
                                        if [Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8].count(14) >= 1 and [Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8].count(17) >= 1:
                                            print("Michal")
                                            michal += 1
print(f"Jonáš: {jonas}")
print(f"Michal: {michal}")
























#strany = [a, b, c, d, e, f, g, h, i]
#if not (strany[0:8].count(14) >= 1 and (strany[0:8].count(15) >= 1 or strany[0:8].count(17) >= 1)):
#    break
#splnuje = True
#for strana in set(strany):
#    if strany.count(strana) == 1:
#        continue
#    elif not (strany.count(strana)*strana) % 4 == 0:
#        splnuje = False
#        break
#if splnuje:
#    print(strany)
#else:
#    break