import random
attempts = 0
winCondition = 0
chance = 0
while attempts <= 129600:
    attempts += 1
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    d = random.randint(1, 6)
    if (a + b + c + d < 9):
        winCondition += 1
chance = winCondition / attempts
chance = round((winCondition / attempts), 3)
if chance > 0.1:
    print("Play")
else:
    print("Don't play")