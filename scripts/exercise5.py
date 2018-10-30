import random

list1 = random.sample(range(100), random.randint(1, 50))
list2 = random.sample(range(100), random.randint(1, 50))
listOverlaps = []

print("list1: " + str(list1))
print("list2: " + str(list2))

for x in list1:
    if x in list2:
        listOverlaps.append(x)

print("listOverlaps: " + str(listOverlaps))
