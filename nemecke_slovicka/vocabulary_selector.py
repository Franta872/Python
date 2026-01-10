import json
import random
import difflib
from pathlib import Path
import constyle as cs

with open(f"{Path(__file__).parent}/vocabulary.json", "r", encoding="utf-8") as f:
    slovicka = json.load(f)
unit_2_3 = slovicka.get("strana_28")

question_type = None
word = None
cz = None
de_visi = None
cz_visi = None
de = None
de_gender = None
description = None

def choose_word():
    question_type = random.choice(["cz", "de"])

    word = random.choice(unit_2_3)
    cz = word.get("cz")
    cz_visi = ", ".join(cz)
    de_visi = []
    de_gender = word.get("gender")
    de = word.get("de")
    if de_gender is None:
        for item in de:
            de_visi.append(item)
    else:
        for x in range(len(word.get("de"))):
            de_visi.append(word.get("gender") + " " + (word.get("de"))[x])
    de_visi = ", ".join(de_visi)
    description = word.get("description")

    return question_type, cz, cz_visi, de, de_gender, de_visi, description



if __name__ == "__main__":
    print(choose_word())