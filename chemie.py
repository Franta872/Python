import random
import time
import constyle as cs
import difflib

prvky = {
"H": { "N": "Vodík", "lat": "Hydrogenium", "Z": 1 },
"He": { "N": "Helium", "lat": "Helium", "Z": 2 },
"Li": { "N": "Lithium", "lat": "Lithium", "Z": 3 },
"Be": { "N": "Beryllium", "lat": "Beryllium", "Z": 4 },
"B": { "N": "Bor", "lat": "Borum", "Z": 5 },
"C": { "N": "Uhlík", "lat": "Carboneum", "Z": 6 },
"N": { "N": "Dusík", "lat": "Nitrogenium", "Z": 7 },
"O": { "N": "Kyslík", "lat": "Oxygenium", "Z": 8 },
"F": { "N": "Fluor", "lat": "Fluorum", "Z": 9 },
"Ne": { "N": "Neon", "lat": "Neon", "Z": 10 },

"Na": { "N": "Sodík", "lat": "Natrium", "Z": 11 },
"Mg": { "N": "Hořčík", "lat": "Magnesium", "Z": 12 },
"Al": { "N": "Hliník", "lat": "Aluminium", "Z": 13 },
"Si": { "N": "Křemík", "lat": "Silicium", "Z": 14 },
"P": { "N": "Fosfor", "lat": "Phosphorus", "Z": 15 },
"S": { "N": "Síra", "lat": "Sulphur", "Z": 16 },
"Cl": { "N": "Chlor", "lat": "Chlorum", "Z": 17 },
"Ar": { "N": "Argon", "lat": "Argon", "Z": 18 },
"K": { "N": "Draslík", "lat": "Kalium", "Z": 19 },
"Ca": { "N": "Vápník", "lat": "Calcium", "Z": 20 },

"Ti": { "N": "Titan", "lat": "Titanium", "Z": 22 },
"V": { "N": "Vanad", "lat": "Vanadium", "Z": 23 },
"Cr": { "N": "Chrom", "lat": "Chromium", "Z": 24 },
"Mn": { "N": "Mangan", "lat": "Manganum", "Z": 25 },
"Fe": { "N": "Železo", "lat": "Ferrum", "Z": 26 },
"Co": { "N": "Kobalt", "lat": "Cobaltum", "Z": 27 },
"Ni": { "N": "Nikl", "lat": "Niccolum", "Z": 28 },
"Cu": { "N": "Měď", "lat": "Cuprum", "Z": 29 },
"Zn": { "N": "Zinek", "lat": "Zincum", "Z": 30 },
"Ga": { "N": "Gallium", "lat": "Gallium", "Z": 31 },
"Ge": { "N": "Germanium", "lat": "Germanium", "Z": 32 },
"As": { "N": "Arsen", "lat": "Arsenicum", "Z": 33 },
"Se": { "N": "Selen", "lat": "Selenium", "Z": 34 },
"Br": { "N": "Brom", "lat": "Bromum", "Z": 35 },
"Kr": { "N": "Krypton", "lat": "Krypton", "Z": 36 },
"Rb": { "N": "Rubidium", "lat": "Rubidium", "Z": 37 },
"Sr": { "N": "Stroncium", "lat": "Strontium", "Z": 38 },

"Mo": { "N": "Molybden", "lat": "Molybdaenum", "Z": 42 },

"Ag": { "N": "Stříbro", "lat": "Argentum", "Z": 47 },
"Cd": { "N": "Kadmium", "lat": "Cadmium", "Z": 48 },
"In": { "N": "Indium", "lat": "Indium", "Z": 49 },
"Sn": { "N": "Cín", "lat": "Stannum", "Z": 50 },
"Sb": { "N": "Antimon", "lat": "Stibium", "Z": 51 },
"Te": { "N": "Tellur", "lat": "Tellurium", "Z": 52 },
"I": { "N": "Jod", "lat": "Iodum", "Z": 53 },
"Xe": { "N": "Xenon", "lat": "Xenon", "Z": 54 },
"Cs": { "N": "Cesium", "lat": "Caesium", "Z": 55 },
"Ba": { "N": "Baryum", "lat": "Barium", "Z": 56 },

"W": { "N": "Wolfram", "lat": "Wolframium", "Z": 74 },
"Os": { "N": "Osmium", "lat": "Osmium", "Z": 76 },

"Pt": { "N": "Platina", "lat": "Platinum", "Z": 78 },
"Au": { "N": "Zlato", "lat": "Aurum", "Z": 79 },
"Hg": { "N": "Rtuť", "lat": "Hydrargyrum", "Z": 80 },
"Tl": { "N": "Thallium", "lat": "Thallium", "Z": 81 },
"Pb": { "N": "Olovo", "lat": "Plumbum", "Z": 82 },
"Bi": { "N": "Bismut", "lat": "Bismuthum", "Z": 83 },
"Po": { "N": "Polonium", "lat": "Polonium", "Z": 84 },
"At": { "N": "Astat", "lat": "Astatium", "Z": 85 },
"Rn": { "N": "Radon", "lat": "Radon", "Z": 86 },
"Fr": { "N": "Francium", "lat": "Francium", "Z": 87 },
"Ra": { "N": "Radium", "lat": "Radium", "Z": 88 }
}
prvky_random = prvky.copy()

print("Toto je program na procvičení prvků z chemie. Bude zadávat jejich název podle značky, nebo naopak.")
input()
cs.clear("line", 2)

nothing = 0
wrong = 0
correct = 0
all = 0
while True:
    if not prvky_random:
        prvky_random = prvky.copy()
    key, value = random.choice(list(prvky_random.items()))
    prvky_random.pop(key)

    question_type = random.choice(["název", "značka"])
    if question_type == "název":
        print(cs.bold("Název prvku: ") + value["N"])
        answer = input("Zadej " + cs.bold(cs.underline("značku prvku")) + ": ")
    else:
        print(cs.bold("Značka prvku: ") + key)
        answer = input("Zadej " + cs.bold(cs.underline("název prvku")) + ": ")
    
    if (key if question_type != "značka" else value["N"]) == answer.strip():
        result = random.choice(["správně!", "správně! Dobrá práce (:", "dobře!"])
        all += 1
        correct += 1
        show_answer = False
    elif (key.lower() if question_type != "značka" else value["N"].lower()) == answer.lower().strip():
        result = random.choice([f"{cs.bold('správně')}, ale pozor na velká a malá písmena.", f"{cs.bold('dobře')}, ale pozor na velikost písmen. Občas to nemusí uznat |:"])
        all += 1
        correct += 1
        show_answer = True
    elif (cs.remove_diacritics(key.lower()) if question_type != "značka" else cs.remove_diacritics(value["N"].lower())) == cs.remove_diacritics(answer.lower().strip()):
        result = random.choice([f"{cs.bold('asi špatně')}. Pozor na velká a malá písmena a ani diakritika tam není.", f"{cs.bold('spíše špatně')}. Je tu absence diakritiky. To už nemusí uznat |:"])
        all += 1
        wrong += 1
        show_answer = True
    elif "" == answer.strip():
        result = random.choice([f"špatně. {cs.bold('Nezadal jsi nic')}!?", f"... {cs.bold('nezadal jsi nic')}, takže asi špatně.", "... dobře, přeskočíme. Jak si přeješ."])
        all += 1
        nothing += 1
        show_answer = False
    elif difflib.SequenceMatcher(None, (key.lower() if question_type != "značka" else value["N"].lower()), answer.strip()).ratio() >= 0.85:
        result = random.choice([f"... asi {cs.bold('správně')}, ale máš tam překlep. Pozor na to."])
        all += 1
        correct += 1
        show_answer = True
    elif 0.4 >= difflib.SequenceMatcher(None, (key.lower() if question_type != "značka" else value["N"].lower()), answer.strip()).ratio() >= 0.85:
        result = random.choice([f"... spíše {cs.bold('špatně')}, máš tam totiž překlep. Pozor na to."])
        all += 1
        wrong += 1
        show_answer = True
    else:
        result = random.choice([f"{cs.bold('blbě')}", f"{cs.bold('hrozně')}", f"{cs.bold('špatně')}", f"prostě {cs.bold('hrozně')}", f"... z tebe {cs.bold('chemik nebude')}"])
        show_answer = True
        wrong += 1
        all += 1
    cs.clear("line", 2)
    print(random.choice([f"Odpověď je", f"Tvá odpověď je", f"Tato odpověď je", f"Tentokrát je to"]), result)
    if show_answer:
        print(f"Tvá odpověď:     {cs.bold(cs.underline(answer))}")
    print(f"""\nZnačka:          {cs.color((cs.bold(cs.underline(key)) if question_type != 'značka' else cs.bold(key)), 'blue')}
Název:           {cs.color((cs.bold(cs.underline(value['N'])) if question_type != 'název' else cs.bold(value['N'])), 'blue')}
Latiský název:   {cs.color(value['lat'], 'red')}
Protonové číslo: {cs.color(value['Z'], 'red')}""")
    again = input(cs.italic('\nZnova? ("n" pro ne, cokoliv jiného pro ano)\nPro zobrazení výsledků zadejte "výsledky"\n'))
    if cs.remove_diacritics(again.strip().lower()) in ["ne", "no", "n", "false", "0", "):", "exit", "ven", "pryc", "out", "nashledanou"]:
        cs.clear("line", 4)
        break
    elif cs.remove_diacritics(again.strip().lower()) == "vysledky":
        cs.clear("line", 11 if show_answer else 10)
        print(f"""Celkový počet prvků: {cs.bold(all)}
{cs.color('Prvky špatně:', 'red')}        {cs.bold(wrong)}
{cs.color('Prvky správně:', 'green')}       {cs.bold(correct)}
{cs.color('Přeskočené prvky:', 'blue')}    {cs.bold(nothing)}""")
        input(cs.italic("\nZmáčkněte 'Enter' pro zpět "))
        cs.clear("line", 6)
    else:
        cs.clear("line", 11 if show_answer else 10)
        continue