def removeDupsWithLists(inputList):
    noDupList = []

    for element in inputList:
        if(element not in noDupList):
            noDupList.append(element)

    return noDupList


def removeDupsWithSets(inputList):
    noDupSet = set(inputList)

    return list(noDupSet)


a = [1, 1, 2, 1, 5, 10, 15, 15, 23, 23, 23, 23, 23, 23, 20, 25]
print("Using Lists: " + str(removeDupsWithLists(a)))
print("Using Sets: " + str(removeDupsWithSets(a)))
