# library for styling text output, but only in terminal

import unicodedata

esc = "\033"
reset= esc+"[0m"

COLORS = {
    "red": esc+"[31m",
    "green": esc+"[32m",
    "yellow": esc+"[33m",
    "blue": esc+"[34m",
    "purple": esc+"[35m",
    "cyan": esc+"[36m",
    "white": esc+"[37m",
}
def color(text, color):
    if color not in COLORS:
        return text
    return COLORS[color] + str(text) + reset

def clear(func="line", num=1):
    if func == "line":
        for x in range(num):
            print(f"{esc}[1A{esc}[2K", end="", flush=True)
    elif func == "screen":
        print(f"{esc}[H{esc}[2J", end="", flush=True)
    elif func == "sym":
        print(f"{esc}[{num}D{esc}[{num}P", end="", flush=True)

def bold(text, bold=True):
    if bold:
        return esc + "[1m" + str(text) + reset
    else:
        return str(text) + reset

# vypíše to jen prázdný řádek, tak to tam asi dávat nebudu
# def weak(text, weak=True):
#     if weak:
#         return esc + "[2m" + str(text) + reset
#     else:
#         return text + reset

def italic(text, italic=True):
    if italic:
        return esc + "[3m" + str(text) + reset
    else:
        return text + reset

def underline(text, underline=True):
    if underline:
        return esc + "[4m" + str(text) + reset
    else:
        return text + reset

# vypíše jen normálí text, tak to asi taky ne
#def flashing(text, flashing=True):
#    if flashing:
#        return esc + "[5m" + str(text) + reset
#    else:
#        return text + reset

def scrossed_out(text, scrossed_out=True):
    if scrossed_out:
        return esc + "[9m" + str(text) + reset
    else:
        return text + reset
    
def cursor(where="left", num1=1, num2=2):
    if where == "left":
        print(esc+f"[{num1}D", end="", flush=True)
    elif where == "right":
        print(esc+f"[{num1}C", end="", flush=True)
    elif where == "down":
        print(esc+f"[{num1}B", end="", flush=True)
    elif where == "up":
        print(esc+f"[{num1}A", end="", flush=True)
    elif where == "coordinates":
        print(esc+f"[{num1};{num2}H", end="", flush=True)

def newLine(num=1):
    for x in range(num):
        print(flush=True)

def letters(text):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    for letter in str(text):
        if letter == "0":
            line1 += "╭───╮"
            line2 += "│   │"
            line3 += "│   │"
            line4 += "│   │"
            line5 += "╰───╯"
        elif letter == "1":
            line1 += "  ╱│ "
            line2 += " ╱ │ "
            line3 += "   │ "
            line4 += "   │ "
            line5 += "   │ "
        elif letter == "2":
            line1 += "╭──╮ "
            line2 += "╵  ╱ "
            line3 += "  ╱  "
            line4 += " ╱   "
            line5 += "╰─── "
        elif letter == "3":
            line1 += " ╭──╮"
            line2 += "    │"
            line3 += "  ──┤"
            line4 += "    │"
            line5 += " ╰──╯"
        elif letter == "4":
            line1 += "  ╱  "
            line2 += " ╱ │ "
            line3 += "└──┼─"
            line4 += "   │ "
            line5 += "   │ "
        elif letter == "5":
            line1 += "┌─────  "
            line2 += "│ ___   "
            line3 += "│╱   ╲  "
            line4 += "      ︳"
            line5 += " ╲___╱  "
        elif letter == "6":
            line1 += "  ╱‾‾   "
            line2 += " ╱      "
            line3 += "│╱‾‾‾╲  "
            line4 += "│     ︳"
            line5 += " ╲___╱  "
        elif letter == "7":
            line1 += "─────┐ "
            line2 += "     ╱ "
            line3 += "    ╱  "
            line4 += "   ╱   "
            line5 += "  ╱    "
        elif letter == "8":
            line1 += "╱‾‾‾╲ "
            line2 += "╲___╱ "
            line3 += "╱   ╲ "
            line4 += "│    │"
            line5 += "╲___╱ "
        elif letter == "9":
            line1 += "╱‾‾‾╲ "
            line2 += "╲___╱ "
            line3 += "    │ "
            line4 += "    │ "
            line5 += " ___╱ "
        elif letter == ":":
            line1 += "   "
            line2 += " • "
            line3 += "   "
            line4 += " • "
            line5 += "   "
        elif letter == ".":
            line1 += "  "
            line2 += "  "
            line3 += "  "
            line4 += "  "
            line5 += "• "
        elif letter == ",":
            line1 += "  "
            line2 += "  "
            line3 += "  "
            line4 += "  "
            line5 += "│ "
        else:
            l = letter
            line1 += l*2+underline(bold("THIS"))+l*3
            line2 += l+underline(bold("SYMBOL"))+l*2
            line3 += l+underline(bold("IS"))+l+underline(bold("NOT"))+l*2
            line4 += l+underline(bold("IN"))+l+underline(bold("THIS"))+l
            line5 += l+underline(bold("LIBRARY"))+l

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

def remove_diacritics(text):
    normalized = unicodedata.normalize("NFD", text)
    return "".join(
        char for char in normalized
        if unicodedata.category(char) != "Mn"
    )