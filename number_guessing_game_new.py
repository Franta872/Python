import random
lower = 0
higher = 100
while True:
    number = random.randint(lower, higher)
    guesses = 0
    while True:
        guess = input(f"Guess number between {lower} and {higher}: ").strip()
        if not guess.isdigit():
            print(f"{guess} is not a valid number.")
            continue
        guess = int(guess)
        if lower > guess or higher < guess:
            print(f"{guess} is not in range.")
            continue
        elif guess > number:
            print("Wrong number, try again lower.")
            guesses += 1
            continue
        elif guess < number:
            print("Wrong number, try again higher.")
            guesses += 1
            continue
        elif guess == number:
            print(f"You win! The number was {number}")
            print(f"It took you {guesses} guesses!")
            break
    if input("Do you want to guess one more number? (y/n)").strip().lower() in ("y", "yes"):
        continue
    else:
        print("Thank's for playing!")
        break