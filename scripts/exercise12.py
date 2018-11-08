def getListEdges(list):
    newList = []

    newList.append(list[0])
    newList.append(list[len(list)-1])
    return newList


a = [5, 10, 15, 20, 25]
print(getListEdges(a))
