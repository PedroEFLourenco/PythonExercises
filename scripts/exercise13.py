def getFibonnaciSequence(sequenceSize):
    startingElement = 1
    fibonnaciSequence = []

    i = 0
    while (i < sequenceSize):
        if len(fibonnaciSequence) <= 1:
            fibonnaciSequence.append(startingElement)
        else:
            fibonnaciSequence.append((fibonnaciSequence[i-1] +
                                     fibonnaciSequence[i-2]))

        i += 1

    return fibonnaciSequence


sizeOfSequence = int(input("Let me know what's the size of the Fibonnaci\
Sequence you want me to generate: "))
print(getFibonnaciSequence(sizeOfSequence))
