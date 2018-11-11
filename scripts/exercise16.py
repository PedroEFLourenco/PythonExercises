
import random
import string


def RandomNumber():
    randomNumber = random.randint(1, 9)
    return randomNumber


def RandomCharacter():
    upOrLowCase = bool(random.getrandbits(1))
    listOfChars = list(string.printable)

    if upOrLowCase:
        letter = listOfChars[random.randint(10, 87)].upper()
    else:
        letter = listOfChars[random.randint(10, 87)]

    return letter


def easyPass():
    listOfPasswords = ["DumpPass101", "EasyPeasy", "qwert123", "suchADumbPass"]
    return listOfPasswords[random.randint(0, len(listOfPasswords)-1)]


def formulatePassword(size):
    password = ""
    while (len(password) < size):
        password += str(RandomCharacter())
        password += str(RandomNumber())

    return password


def validateSize(userInput):
        try:
            value = int(userInput)
            if value < 16:
                return False
            return True
        except ValueError:
            return False


def main():
    print("-------------Password Generator v1-------------")

    while (1):
        hardOrEasy = input("Do you want a simple Password?(Y/N)): ").upper()
        if hardOrEasy in ("Y", "N"):
            break

    if hardOrEasy == "Y":
        print(easyPass())
    else:
        validSize = False
        while not validSize:
            size = input("What size would it be nice for you?(16<) ")
            validSize = validateSize(size)

        print(formulatePassword(int(size)))


main()
