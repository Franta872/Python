import random
import time
import difflib
import constyle as cs
import vocabulary_selector as vc

question_type, cz, de_gender, de_word, de_visi, description = vc.choose_word()
print(question_type, cz, de_gender, de_word, de_visi, description, sep="\n")
input()

while True:
    cz, de = random.choice(list(vocabulary.items()))
    cz_visi, de_visi = map(lambda x: x if type(x) == str else ", ".join(x), [cz, de])

    question_type = random.choice(["de", "cz"])
    if question_type == "de":
        print("němčina:", de_visi)
        answer = input("český překlad: ").strip()
    else:
        print("čeština:", cz_visi)
        answer = input("německý překlad: ").strip()
    cs.clear("line", 2)

    long_var = de if question_type != "de" else cz
    long_var = [long_var, "↔"] if type(long_var) == str else long_var
    lower_long_var = tuple(map(lambda x: x.lower(), long_var))
    similarity = max(map(lambda x: difflib.SequenceMatcher(None, answer.lower(), x).ratio(), lower_long_var))
    
    show_answer = False
    if answer in long_var:
        result = "správně!"
    elif "" == answer:
        result = "špatně, nic jsi nenapsal."
    elif answer.lower() in map(lambda x: x.lower(), lower_long_var):
        result = "správně, ale velikost písmen dělá problémy |:"
        show_answer = True
    elif cs.remove_diacritics(answer.lower()) in map(lambda x: cs.remove_diacritics(x), lower_long_var):
        result = "asi ještě správně, ale diakritika dělá problémy."
        show_answer = True
    elif similarity >= 0.8:
        result = "spíše správně, ale je tam gramatická chyba."
        show_answer = True
    elif 0.65 <= similarity < 0.8:
        result = "spíše špatně, ale je to podobné výsledku."
    else:
        result = "prostě špatně!"
        show_answer = True

    #cz_visi, de_visi = map(lambda y: cs.bold(cs.color(cs.underline(y) if question_type == f"{y=}".split("_")[0] else y, "red")), [cz_visi, de_visi])
    cz_visi = cs.bold(cs.color(cs.underline(cz_visi) if question_type != "cz" else cz_visi, "red"))
    de_visi = cs.bold(cs.color(cs.underline(de_visi) if question_type != "de" else de_visi, "red"))
    
    print(f"Výsledek je {result}")
    print("Tvá odpověď: " + answer + "\n" if show_answer else "")
    print(f"Slovo německy:  {de_visi}\nSlovo česky:    {cz_visi}\n")
    
    again = input("Znova? (ne pro ne)\n")
    if cs.remove_diacritics(again.lower().strip()) in ("ne", "nein", "no", "n"):
        break
    else:
        cs.clear("line", 8)
        continue