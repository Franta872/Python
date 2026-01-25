import time

start_time = time.time()
n = 3
print(2)
num = 1

while (time.time() - start_time) < 60:
    je_prvocislo = True
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            je_prvocislo = False
            break
    if je_prvocislo:
        print(n)
        num += 1
    n += 2
print(f"\nNumber of found prime numbers: {num}")