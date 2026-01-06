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

original_time = f"Original time: {cs.bold(f'{timee//3600:02}')}:{cs.bold(f'{(timee//60) % 60:02}')}:{cs.bold(f'{timee % 60:02}')}"
start = time.perf_counter()
remaining = timee
while not remaining <= 0:
    remaining = int(round(timee - (time.perf_counter() - start), 2)*100)
    cs.clear("line", 8)
    centis = remaining%100
    seconds = (remaining//100) % 60
    minutes = ((remaining//100)//60) % 60
    hours = (remaining//100)//3600
    print(original_time)
    print((50-round((remaining/(timee*100))*50))*cs.color('▇', "blue"), round((remaining/(timee*100))*50)*cs.color('▇', "red")+"\n",sep=cs.color('▇', "cyan"))
    cs.letters(f"{hours:02}:{minutes:02}:{seconds:02}.{centis:02}")
    time.sleep(0.0096)

cs.clear("line", 8)
print(original_time)
print(cs.bold(cs.underline(cs.color("ČAS JE U KONCE!", "blue"))))