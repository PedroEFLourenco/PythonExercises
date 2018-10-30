number = int(input("Sir, give me a number for me to check its divisors: "))

allNumberList = range(1, number+1)
divisorsList = []

for x in allNumberList:
    if ((number % x) == 0):
        divisorsList.append(x)


print(*divisorsList)
