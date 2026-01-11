import json
import random
from pathlib import Path
import constyle as cs
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

with open(resource_path("vocabulary.json"), "r", encoding="utf-8") as f:
    lekce = json.load(f)

#with open(f"{Path(__file__).parent}/vocabulary.json", "r", encoding="utf-8") as f:
#    lekce = json.load(f)
unit_2_3 = []
for strana in lekce.values():
    for slovo in strana:
        unit_2_3.append(slovo)
unit_2_3_copy = unit_2_3.copy()

#question_type = None
#word = None
#cz = None
#de_visi = None
#cz_visi = None
#de = None
#de_gender = None
#de_gender_visi = None
#description = None

def choose_word():
    question_type = random.choice(["cz", "de"])

    global unit_2_3_copy
    if not unit_2_3_copy:
        unit_2_3_copy = unit_2_3.copy()
    word = random.choice(unit_2_3_copy)
    unit_2_3_copy.remove(word)

    cz = word.get("cz")
    cz_visi = cs.bold(", ".join(cz))
    de_visi = []
    de_gender = word.get("gender")
    de = word.get("de")
    if de_gender == "der":
        de_gender_visi = cs.color(de_gender, "blue")
    elif de_gender == "die":
        de_gender_visi = cs.color(de_gender, "red")
    elif de_gender == "das":
        de_gender_visi = cs.color(de_gender, "green")
    else:
        de_gender_visi = None
    if de_gender is None:
        for item in de:
            de_visi.append(item)
    else:
        for x in range(len(word.get("de"))):
            de_visi.append(f"{de_gender_visi} {cs.bold((word.get('de'))[x])}")
    de_visi = cs.bold(", ".join(de_visi))
    description = word.get("description")

    return question_type, cz, cz_visi, de, de_gender, de_gender_visi, de_visi, description


if __name__ == "__main__":
    print(choose_word())