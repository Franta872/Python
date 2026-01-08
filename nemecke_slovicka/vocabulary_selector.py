import json
import random
import difflib

with open("vocabulary.json", "r", encoding="utf-8") as f:
    slovicka = json.load(f)
unit_2_3 = slovicka.get("lekce_2.3")

cz = None
de = None
de_visi = None
de_gender = None
de_word = None
description = None

def choose_word():
    question_type = random.choice(["cz", "de"])

    cz, de = random.choice(list(unit_2_3.items()))
    de_visi = de.get("de") if de.get("gender") == None else de.get("gender")+" "+de.get("de")
    de_gender = de.get("gender")
    de_word = de.get("de")
    description = de.get("description")

    return question_type, cz, de_gender, de_word, de_visi, description




if __name__ == "__main__":
    print(cz)
    print(de)
    print(de_visi)