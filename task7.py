import random

result = round(((1 / 3) - (1 / 36)), 3)
k = 0
number = 0
chance = 0
while not chance == result:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    if (a == 6 or b == 6):
        number += 1
    k += 1
    if not number == 0:
        chance = round((number/k), 3)
print("Chance of getting six:", chance)
print("Number of attempts:", k)