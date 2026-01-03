import random
import constyle as cs

# print("Toto je program na procvičení prvků z chemie. Bude zadávat jejich název podle značky, nebo naopak.")

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


wrong = 0
correct = 0
all = 0
while True:
    key, value = random.choice(list(prvky.items()))
    
    if random.randint(0, 1) == 1:
        print("Název prvku: " + value["N"])
        answer = input("Zadej značku prvku: ")
    else:
        print("Značka prvku: " + key)
        answer = input("Zadej název prvku: ")
    if key.strip() == answer.strip():
        result = random.choice(["správně!", "správně! Dobrá práce (:", "dobře!"])
        all += 1
    elif key.lower().strip() == answer.lower().strip():
        result = random.choice(["správně, ale pozor na velká a malá písmena.", "dobře, ale pozor na velká a malá písmena. Občas to nemusí uznat |:"])
        all += 1
    elif key.strip() == "":
        result = random.choice(["špatně. Nezadal jsi nic!?", "... nezadal jsi nic, takže asi špatně."])
        all += 1
    else:
        result = random.choice(["blbě", "hrozně", "špatně", "prostě hrozně", "... z tebe chemik nebude"])
        wrong += 1
        all += 1
    print("Je to " + result)
    again = input("Znova? ")
    if again == "Ano":
        continue
    else:
        break