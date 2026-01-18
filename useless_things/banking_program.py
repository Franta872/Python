import constyle as cs
import credit_card_validation as ccv
import time

money = 0

def menu():
    print("*"*40)
    print("1. Zjistit " + cs.bold("stav účtu"))
    print("2. Vybrat " + cs.bold("peníze z účtu"))
    print("3. Vložit " + cs.bold("peníze na účet"))
    print("4. Zkontrolovat " + cs.bold("platnost platební karty"))
    print("5. Exit")
    print("*"*40)
    print(cs.italic("Vyberte " + cs.bold("číslo 1 – 5") + "\n"))
    while True:
        action = input("Vyber číslo od 1 do 5: ")
        if not action.isdigit():
            print("Musí to být číslo!")
            time.sleep(2)
            cs.clear("line", 2)
            continue
        elif 1 > int(action) or int(action) > 5:
            print("Číslo musí být v rozmezí 1 až 5")
            time.sleep(2)
            cs.clear("line", 2)
            continue
        action = int(action)
        break
    cs.clear("line", 10)
    match action:
        case 1:
            account_status()
        case 2:
            withdraw_money()
        case 3:
            deposit_money()
        case 4:
            card_validation()
        case 5:
            exit()

def account_status():
    print("*"*40)
    print(f"{f'Stav účtu: {money:.2f} Kč':^40}")
    print("*"*40+"\n")
    input(cs.italic("Enter pro zpět do menu "))
    cs.clear("line", 5)
    menu()

def withdraw_money():
    print("*"*40)
    print(f'{"Kolik chete vybrat?":^40}')
    print("*"*40+"\n")
    global money
    while True:
        withdraw = input("Zadej částku v Kč: ")
        if not withdraw.isdigit():
            print("Musí to být číslo!")
            time.sleep(2)
            cs.clear("line", 2)
            continue
        elif int(withdraw) > money:
            print("Nesmíš jít do mínusu")
            time.sleep(2)
            cs.clear("line", 2)
            continue
        withdraw = int(withdraw)
        break
    cs.clear("line", 5)
    money -= withdraw
    print("*"*40)
    print(f'{"Peníze byli úspěšně vybrány!":^40}')
    print("*"*40)
    input(cs.italic("Enter pro zpět do menu: "))
    cs.clear("line", 4)
    menu()

def deposit_money():
    print("*"*40)
    print(f'{"Kolik chete vložit?":^40}')
    print("*"*40+"\n")
    while True:
        deposit = input("Zadej částu v Kč: ")
        if not deposit.isdigit():
            print("Částka musí být číslo!")
            time.sleep(2)
            cs.clear("line", 2)
            continue
        deposit = int(deposit)
        break
    cs.clear("line", 5)
    global money
    money += deposit
    print("*"*40)
    print(f'{"Peníze byli úspěšně vloženy!":^40}')
    print("*"*40)
    input(cs.italic("Enter pro zpět do menu: "))
    cs.clear("line", 4)
    menu()

def card_validation():
    print("*"*40)
    print(f'{"Jakou kartu chete ověřit?":^40}')
    print("*"*40+"\n")
    while True:
        card = input("Zadejte číslo karty: ").replace("-", "").replace(" ", "")
        if not card.isdigit():
            print("Číslo karty musí být číslo!")
            time.sleep(2)
            cs.clear("line", 2)
            continue
        elif not len(card) == 16:
            print("Číslo karty musí být dlouhé 16 znaků!")
            time.sleep(2)
            cs.clear("line", 2)
            continue
        cs.clear("line", 5)
        break
    if ccv.card_check(card) == "VALID":
        validity = "platné"
    else:
        validity = "neplatné"
    print("*"*40)
    print(f'{f"Číslo karty je {validity}":^40}')
    print("*"*40+"\n")
    input(cs.italic("Enter pro zpět do menu: "))
    cs.clear("line", 5)
    menu()

menu()