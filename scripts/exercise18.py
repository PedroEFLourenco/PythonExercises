import random


def validateNumber(userInput):
        try:
            value = int(userInput)
            if value < 1000 or value > 9999:
                return False
            return True
        except ValueError:
            return False


def countCows(solution, guessedNumber):
    guessedList = list(str(guessedNumber))
    solutionList = list(str(solution))

    cowList = [cow for idx, cow in enumerate(guessedList) if
               cow == solutionList[idx]]

    return len(cowList)


def countBulls(solution, guessedNumber):
    guessedList = list(str(guessedNumber))
    solutionList = list(str(solution))

    bullList = [bull for idx, bull in enumerate(guessedList) if
                bull != solutionList[idx] and bull in solutionList]

    return len(bullList)


def main():
    print("Welcome to the game of Cows and Bulls")
    gameOver = False
    tries = 0
    solution = random.randint(0000, 9999)
    while not gameOver:
        guessedNumber = input("Please guess a number: ")
        if validateNumber(guessedNumber):
            cows = countCows(solution, guessedNumber)
            bulls = countBulls(solution, guessedNumber)
        else:
            print("Invalid number. You do know how to play this, right? ")
            continue

        print(str(cows) + " cows," + str(bulls) + " bulls")

        if cows == len(list(str(solution))):
            tries += 1
            print("You won the game of Cows and Bulls!")
            print("Took you " + str(tries) + " tentatives!")
            gameOver = True
        else:
            tries += 1


main()
