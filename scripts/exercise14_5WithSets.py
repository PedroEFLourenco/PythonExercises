import random


def ListOverlaps(inputList1, inputList2):
    set1 = set(inputList1)
    set2 = set(inputList2)
    listOverlaps = list(set(set1).intersection(set2))

    return list(listOverlaps)


list1 = random.sample(range(100), random.randint(1, 50))
list2 = random.sample(range(100), random.randint(1, 50))

print("list1: " + str(list1))
print("list2: " + str(list2))

list3 = ListOverlaps(list1, list2)
print("listOverlaps: " + str(list3))
