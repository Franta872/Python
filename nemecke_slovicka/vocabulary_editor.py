# toto je program, který vytvoří JSON pro další program
import json
import constyle as cs
import pyperclip #pip install pyperclip

nazev_strany = f"strana_{input('Jaké je číslo strany?: ')}"
words_list = []
word_dict = {}

while True:
    cz = input(f"Zadejte {cs.bold('české')} slova: ")
    cz = cz.split(";")
    de = input(f"Zadejte {cs.bold('německé')} slova: ")
    de = de.split(";")
    gender = input(f"Zadejte {cs.bold('rod')} slova: ").strip().lower()
    if gender == "":
        gender = None
    description = input(f"Zadejte {cs.bold('popis')} slova: ").strip().lower()
    if description == "":
        description = None
    word_dict.update({"cz": cz})
    word_dict.update({"de": de})
    word_dict.update({"gender": gender})
    word_dict.update({"description": description})
    words_list.append(word_dict.copy())
    word_dict.clear()
    if input("Chceš pokračovat? (ne pro ne): ").strip().lower() in ["ne", "n", "no", "nein"]:
        break

json_text = json.dumps({nazev_strany: words_list}, ensure_ascii=False, indent=2)
pyperclip.copy(json_text)
print(json_text)