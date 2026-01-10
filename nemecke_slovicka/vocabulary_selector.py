import json
import random
import difflib
from pathlib import Path
import constyle as cs

with open(f"{Path(__file__).parent}/vocabulary.json", "r", encoding="utf-8") as f:
    slovicka = json.load(f)
unit_2_3 = slovicka.get("lekce_2.3")

cz = None
de = None
de_visi = None
cz_visi = None
de_gender = None
de_word = None
description = None

def choose_word():
    question_type = random.choice(["cz", "de"])

    cz, de = random.choice(list(unit_2_3.items()))
    cz = cz.split(";") if ";" in cz else [cz]
    cz_visi = ", ".join(cz)
    de_visi = []
    if de.get("gender") is None:
        for word in de.get("de"):
            de_visi.append(word)
    else:
        for x in range(len(de.get("de"))):
            de_visi.append((de.get("gender")) + " " + (de.get("de"))[x])
    de_visi = ", ".join(de_visi)
    de_gender = de.get("gender")
    de_word = de.get("de")
    description = de.get("description")

    return question_type, cz, cz_visi, de, de_gender, de_word, de_visi, description



if __name__ == "__main__":
    print(cz)
    print(de)
    print(de_visi)