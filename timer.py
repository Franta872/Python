# timer
import time
import constyle as cs

while True:
    timee = input("Zadej čas v sekudách: ")
    if not timee.isdigit():
        print("Čas musí být číslo")
        continue
    elif int(timee) == 0:
        print("Čas nesmí být 0")
        continue
    else:
        timee = int(timee)
        break

for x in range(timee*100, -1, -1):
    cs.clear("line", 8)
    mili = x%100
    seconds = (x//100) % 60
    minutes = ((x//100)//60) % 60
    hours = (x//100)//3600
    print(f"Original time: {cs.bold(f'{timee//3600:02}')}:{cs.bold(f'{(timee//60) % 60:02}')}:{cs.bold(f'{timee % 60:02}')}")
    print((50-round((x/(timee*100))*50))*cs.color('▇', "blue"), round((x/(timee*100))*50)*cs.color('▇', "red"),sep=cs.color('▇', "cyan"))
    print()
    cs.letters(f"{hours:02}:{minutes:02}:{seconds:02}.{mili:02}")
    time.sleep(0.0093)

cs.clear("line", 8)
print(f"Original time: {cs.color(cs.bold(f'{timee//3600:02}'), 'red')}:{cs.color(cs.bold(f'{(timee//60) % 60:02}'), 'red')}:{cs.color(cs.bold(f'{timee % 60:02}'), 'red')}")
print(cs.bold(cs.underline(cs.color("ČAS JE U KONCE!", "blue"))))