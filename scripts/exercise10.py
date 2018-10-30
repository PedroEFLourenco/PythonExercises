import random

listOne = random.sample(range(20), random.randint(1, 10))
listTwo = random.sample(range(20), random.randint(1, 10))

listOverlaps = [number for number in listOne if number in listTwo]

print(*listOne)
print(*listTwo)
print(*listOverlaps)
