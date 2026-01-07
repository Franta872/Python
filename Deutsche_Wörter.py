import random
import time
import difflib
import constyle as cs

vocabulary = {
    #"ne": ("nein"),
    #"ano": ("ja"),
    #"a": ("und"),
    #"já": ("ich"),
    #"ty": ("du"),
    #"on": ("er"),
    ("ona", "oni"): ("sie"),
    #"ono": ("es"),
    #"my": ("wir"),
    #"vy": ("ihr"),
    #"Vy": ("Sie")
}


while True:
    cz, de = random.choice(list(vocabulary.items()))
    cz_visi, de_visi = map(lambda x: x if type(x) == str else ", ".join(x), [cz, de])

    question_type = random.choice(["de", "cz"])
    if question_type == "de":
        print("němčina:", de_visi)
        answer = input("český překlad: ")
    else:
        print("čeština:", cz_visi)
        answer = input("německý překlad: ")
    cs.clear("line", 2)
    lang_var = (de if question_type != "de" else cz)
    if answer.strip() in lang_var:
        result = "správně!"
    elif answer.lower().strip() in tuple(map(lambda x: x.lower(), lang_var)):
        result = "správně, ale velikost písmen dělá problémy |:"
    elif cs.remove_diacritics(answer.strip()) in tuple(map(lambda x: cs.remove_diacritics(x.lower()), lang_var)):
        result = "asi ještě správně, ale diakritika dělá problémy."
    elif "" == answer.strip().lower():
        result = "špatně, nic jsi nenapsal."
    else:
        result = "prostě špatně!"

    #cz_visi, de_visi = map(lambda y: cs.bold(cs.color(cs.underline(y) if question_type == f"{y=}".split("_")[0] else y, "red")), [cz_visi, de_visi])
    cz_visi = cs.bold(cs.color(cs.underline(cz_visi) if question_type != "cz" else cz_visi, "red"))
    de_visi = cs.bold(cs.color(cs.underline(de_visi) if question_type != "de" else de_visi, "red"))
    
    print(f"""Výsledek je {result}
Slovo německy: {de_visi}
Slovo česky:   {cz_visi}\n""")
    
    again = input("Znova? (ne pro ne)\n")
    if cs.remove_diacritics(again.lower().strip()) in ("ne", "nein", "no", "n"):
        break
    else:
        cs.clear("line", 8)
        continue