import random
import time
import constyle as cs

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}

words = ["apple", "banana", "computer", "school", "alien", "blue", "secret", "password"]

hangman_state = 0
random_word = random.choice(words)
underscore_word = ["_"]*len(random_word)
message = "Welcome to the hangman game!"
wrong_letters = []

while True:
    print(message)
    print("*"*30)
    print(hangman_art[hangman_state][0], f"{'Wrong letters: ' + ', '.join(wrong_letters):>26}" if wrong_letters else "")
    print(hangman_art[hangman_state][1])
    print(hangman_art[hangman_state][2], f"{' '.join(underscore_word):>26}")
    print("*"*30)
    letter = input("Enter letter: ").strip().lower()
    if letter == "":
        print("You must enter SOMEthing and not NOthing!")
        time.sleep(2)
        cs.clear("line", 8)
        continue
    elif len(letter) != 1:
        print(f"Letter must be only 1 letter long and not {len(letter)}!")
        time.sleep(2.5)
        cs.clear("line", 8)
        continue
    elif letter in underscore_word or letter in wrong_letters:
        print(f"You already guessed this letter!")
        time.sleep(2.5)
        cs.clear("line", 8)
        continue

    if letter in random_word:
        for x in range(len(random_word)):
            if random_word[x] == letter:
                underscore_word[x] = letter
        message = f"You're right, the letter {letter} is in the word!"
    else:
        wrong_letters.append(letter)
        hangman_state += 1
        message = f"You're wrong, the letter {letter} isn't in the word!"
    cs.clear("line", 8)
    if "".join(underscore_word) == random_word:
        print("You won, you're a winner!!!!!!!!")
        break
    elif hangman_state >= len(hangman_art):
        print("You lost, you're a loser!!!!!!!")
        break
    continue
print(f"The word was {cs.bold(random_word)}")