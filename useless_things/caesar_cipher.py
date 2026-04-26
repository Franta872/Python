from string import ascii_lowercase, ascii_uppercase

cipher = input("Input cipher: ")
try:
    moveBy = int(input("Enter by how many letters you want to move: "))
except ValueError:
    print("That's not a number!")

lowercase = ascii_lowercase * (int(abs(moveBy)/26) + 2)
uppercase = ascii_uppercase * (int(abs(moveBy)/26) + 2)

text = ""
for x in cipher:
    if x in ascii_lowercase:
        text += lowercase[lowercase.index(x)+moveBy]
    elif x in ascii_uppercase:
        text += uppercase[uppercase.index(x)+moveBy]
    else:
        text += x

print(text)