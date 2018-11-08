def getDivisors(number):
    allNumberList = range(1, number+1)
    divisorsList = []

    for x in allNumberList:
        if ((number % x) == 0):
            divisorsList.append(x)

    return divisorsList


num = int(input("Please tell me a number so I can check if it is a prime: "))
divisors = getDivisors(num)

if (len(divisors) > 2):
    print(str(num) + " is not a Prime Number")
else:
    print(str(num) + " is a Prime Number")
