import random
options = ("stone", "scissors", "paper")

while True:
    computer = random.choice(options)
    human = None
    while True:
        human = input(f"Enter {", ".join(options)}: ").strip().lower()
        if human not in options:
            print(f"{human} is not valid.")
            continue
        else:
            break
    result = None
    if human == computer:
        result = "It's a tie!"
    elif (human == "paper" and computer == "stone") or (human == "scissors" and computer == "paper") or (human == "stone" and computer == "scissors"):
        result = "You win!"
    else:
        result = "You lose!"
    print(f"Computer: {computer}, you: {human}")
    print(result)
    if input("Do you want to continue? (y/n) ").lower().strip() in ("y", "yes", "ano", "ja"):
        continue
    else:
        break