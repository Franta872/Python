from sys import exit

nonNum = ("+", "-", "*", "/", "(", ")")

equation = "("+input("Enter equation: ").strip().replace(",", ".")+")"

listEqu = []
# tokenization
start = None
num = False
for x, i in zip(equation[1:-1], range(1, len(equation)-1)):
    if equation[i:i+2] == "**" and listEqu[-1] != "**": # **
        listEqu.append("**")
    elif not num and x in nonNum and (len(listEqu) == 0 or listEqu[-1] != "**"): # + - * /
        listEqu.append(x)
        continue
    if (x.isdecimal() or x == ".") and not num: # start number
        start = i
        num = True
    if not (equation[i+1].isdecimal() or equation[i+1] == ".") and num: # end number
        num = False
        #thisNum = equation[start-1:i+1] if equation[start-1] in ["+", "-"] and equation[start-2] == "(" else equation[start:i+1]
        if equation[start-1] in ["+", "-"] and equation[start-2] == "(":
            listEqu.pop(-1)
            thisNum = equation[start-1:i+1]
        else:
            thisNum = equation[start:i+1]
        
        listEqu.append(int(thisNum) if equation[start:i+1].isdecimal() else float(thisNum))
        start = None

# finding max. level of parentheses
print(listEqu)
# PH == parentheses
maxPH = 0
if "(" in listEqu and ")" in listEqu:
    PHlayer = 0
    for x in listEqu:
        if x == "(":
            PHlayer += 1
            if PHlayer > maxPH:
                maxPH = PHlayer
        elif x == ")":
                PHlayer -= 1

# calculation
def calculation(Equ: list, start = 0, end = -1) -> list:
    try:
        plusMinus = []
        MultDivision = []
        powers = []
        for x in listEqu[start:end]:
            if x == "+" or x == "-":
                plusMinus.append(x)
            elif x == "*" or x == "/":
                MultDivision.append(x)
            elif x == "**":
                powers.append(x)
        for operator in powers + MultDivision + plusMinus:
            operatorIndex = Equ[start:end].index(operator)
            firstNum = Equ[operatorIndex-1]
            secondNum = Equ[operatorIndex+1]
            result = None
            match operator:
                case "+":
                    result = firstNum + secondNum
                case "-":
                    result = firstNum - secondNum
                case "*":
                    result = firstNum * secondNum
                case "/":
                    result = firstNum / secondNum
                case "**":
                    result = firstNum ** secondNum
            Equ.pop(operatorIndex)
            Equ.pop(operatorIndex)
            Equ.pop(operatorIndex-1)
            Equ.insert(operatorIndex, result)
        return Equ
    except TypeError:
        exit(f"Incorrect input")

if maxPH == 0:
    listEqu = calculation(listEqu)
else:
    pass


print(listEqu, maxPH)