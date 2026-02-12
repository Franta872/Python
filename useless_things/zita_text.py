# tento program udělá z normální textu takový text, jako by ho psala Zita (prostě hrozné)
import random
import unicodedata

# config:
punctuation = True                # funkce na mazání interpunkce
punctuation_percent = 95          # kolik procent interpunkce se smaže

diacritics = True                 # funkce na mazání dikaritiky
diacritics_percent = 99           # kolik procent diakritiky se má mazat

lower_text = True                 # funkce na zmenšení textu
lower_text_percent = 95           # o kolik procent to zemnší text

reshuffling = True                # přehazování symbolů
reshuffling_per_symbols = 15      # po kolika symbolech se mají znaky přehazovat

adding_spaces = True              # přidávání dvojích mezer
adding_spaces_percent = 28        # kolik mezer se změní na 2 v procentech

number_change = True              # změna cifer číslic (odečtení a přičtení)
number_change_percent = 38       # šance na změnu cifer číslic
number_change_max = 1             # max rozsah změny cifer číslic,
                                  # např. když je 2, tak číslo 5 může být 3 až 7


input_text = input("Zadejte text: ").strip()

# tato funkce z procent udělá výsledek (True/False)
def percentage(procento=80):
    if random.randint(1, 100) <= procento:
        return True
    else:
        return False


# Mazání interpunkce (to je ztráta času!) (,.:;?!–()„“"")
if punctuation:
    punctuation_symbols = (",", ".", ":", ";", "?", "!", "–", "(", ")", "„", "“", '"', "'")
    text_no_punctuation = ""
    for symbol in input_text:
        if not (symbol in punctuation_symbols and percentage(punctuation_percent)):
            text_no_punctuation += symbol
    input_text = text_no_punctuation

# Mazání diakritiky (ta ještě existuje?) (ěščřžýáíéňúůß a speciální znaky)
if diacritics:
    text_no_no_diacritics = ""
    for symbol in input_text:
        text_no_no_diacritics += unicodedata.normalize("NFKD", unicodedata.normalize("NFD", symbol)[0] if percentage(diacritics_percent) else symbol)
    input_text = text_no_no_diacritics

# Zmenšení velkých písmen (ta se přece nepíší)
if input_text:
    text_lower = ""
    for symbol in input_text:
        if symbol != symbol.lower() and percentage(lower_text_percent):
            text_lower += symbol.lower()
        else:
            text_lower += symbol
    input_text = text_lower

# Náhodné přehazovaní písmen (chyby se nikdy nekontrolují)
if reshuffling:
    text_reshuffled = list(input_text)
    for y in [(x, x+reshuffling_per_symbols) for x in range(0, len(text_reshuffled)//reshuffling_per_symbols*reshuffling_per_symbols, reshuffling_per_symbols)]:
        index = random.randint(y[0], y[1]-1) if reshuffling_per_symbols != 1 else y[0]
        a = text_reshuffled[index-1]
        text_reshuffled[index-1] = text_reshuffled[index]
        text_reshuffled[index] = a

    input_text = "".join(text_reshuffled)

# Náhodné přidávání mezer, protože to vypadá hůř a lidi to dělají (:
if adding_spaces:
    text_add_space = ""
    for symbol in range(len(input_text)):
        if input_text[symbol] == " " and \
        not (input_text[symbol+1] == " " if symbol != 0 else True) and \
        percentage(adding_spaces_percent):
            text_add_space += "  "
        else:
            text_add_space += input_text[symbol]
    input_text = text_add_space

# Občas se i čísla dají napsat špatně a kontrola je přece zbytečná
if number_change:
    text_number_change = ""
    for symbol in input_text:
        if symbol.isdigit() and percentage(number_change_percent):
            text_number_change += str(abs(random.randint(int(symbol)-number_change_max, int(symbol)+number_change_max)))
        else:
            text_number_change += symbol
    input_text = text_number_change


print(input_text)