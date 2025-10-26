rolls = []
import random
while True:
    roll = random.randint(1, 6)
    rolls.append(roll)
    if roll == 6:
        break
print(rolls)