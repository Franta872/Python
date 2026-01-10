import random
import time
import difflib
import constyle as cs
import vocabulary_selector as vc


while True:
    question_type, cz, cz_visi, de, de_gender, de_word, de_visi, description = vc.choose_word()
    #print(question_type, cz, de, de_gender, de_word, de_visi, description, sep="\n")    
    
    print((print("němčina: " + de_visi) if description is None else f"němčina ({description}): " + de_visi)  if question_type == "de" else "čeština: "+cz_visi)
    
    result_gender = None
    if question_type != "de" and de_gender != None:
        while True:
            answer_gender = input("Zadej rod slova (der, die, das): ").lower().strip()
            if answer_gender in ["der", "die", "das"]:
                break
            else:
                cs.clear("line", 1)
                continue
        if answer_gender == de_gender:
            result_gender = "správně!"
        else:
            result_gender = "špatně! Měl být " + de_gender

    if question_type == "de":
        answer = input("český překlad: ").strip()
    elif question_type == "cz":
        answer = input("německý překlad: ").strip()

    lang_var = de_word if question_type != "de" else cz
    similarity = max(difflib.SequenceMatcher(None, answer.lower(), (de_word[x] if question_type != "de" else cz[x]).lower()).ratio() for x in range(len(de_word)))

    show_answer = False
    if answer in lang_var:
        result = "správně!"
    elif "" == answer:
        result = "špatně, nic jsi nenapsal."
    elif answer.lower() in [x.lower() for x in lang_var]:
        result = "správně, ale velikost písmen dělá problémy |:"
        show_answer = True
    elif cs.remove_diacritics(answer) in [cs.remove_diacritics(x) for x in lang_var]:
        result = "asi ještě správně, ale diakritika dělá problémy."
        show_answer = True
    elif cs.remove_diacritics(answer.lower()) in [cs.remove_diacritics(x.lower()) for x in lang_var]:
        result = "špatně, je tu problém ve velikosti písmen a ani diakritika tam není."
        show_answer = True
    elif similarity >= 0.8:
        result = "spíše správně, ale je tam gramatická chyba."
        show_answer = True
    elif 0.7 <= similarity < 0.8:
        result = "spíše špatně, ale je to podobné výsledku."
    else:
        result = "prostě špatně!"
        show_answer = True

    #cz_visi, de_visi = map(lambda y: cs.bold(cs.color(cs.underline(y) if question_type == f"{y=}".split("_")[0] else y, "red")), [cz_visi, de_visi])
    cz_visi = cs.bold(cs.color(cs.underline(cz_visi) if question_type != "cz" else cz_visi, "red"))
    de_visi = cs.bold(cs.color(cs.underline(de_visi) if question_type != "de" else de_visi, "red"))
    cs.clear("line", 3)

    print(f"Rod je {result_gender}") if result_gender != None else None
    print(f"Slovíčko je {result}")
    print("Tvá odpověď: " + answer + "\n" if show_answer else "")
    print(f"Slovo německy:  {de_visi}\nSlovo česky:    {cz_visi}\n")
    
    again = input("Znova? (ne pro ne)\n")
    if cs.remove_diacritics(again.lower().strip()) in ("ne", "nein", "no", "n"):
        break
    else:
        cs.clear("line", 9)
        continue