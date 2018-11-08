def YodaMyString(inputString):
    import numpy

    Yodized = reversed(numpy.asarray(inputString.split()))

    yodaString = " ".join(list(Yodized))

    return yodaString


toReverse = str(input("Please, provide a string for master yoda to reverse: "))
print("Master Yoda says: " + YodaMyString(toReverse))
