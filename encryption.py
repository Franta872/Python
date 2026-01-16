import random
import string

chars = list(string.printable.strip() + " ěščřžýáíéúůĚŠČŘŽÝÁÍÉÚŮäëüößÄËÜÖ")
key = chars.copy()
random.shuffle(key)
plain_text = input("Enter text to encrypt: ").strip()
arent = []
for x in plain_text:
    if x not in list(chars):
        arent.append(x)
if arent != []:
    print("Sorry, you can't you these symbols: " + ", ".join(arent))
    exit()
cipher_text = ""

for x in plain_text:
    cipher_text += key[chars.index(x)]

print(cipher_text)
plain_text = ""
for x in cipher_text:
    plain_text = plain_text + chars[key.index(x)]
print(plain_text)