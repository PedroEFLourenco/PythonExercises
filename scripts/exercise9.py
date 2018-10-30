import random

correct = False
randomNumber = random.randint(1, 9)
tries = 0
while not correct:

    userNumber = int(input("Between 1 and 9, guess the number i am thinking of:\
 "))

    if randomNumber > userNumber:
            print("It's Higher than that")
    elif randomNumber < userNumber:
            print("It's Lower than that")
    else:
        print("You Bloody Genius, that's correct!!!")
        correct = True

    tries += 1

print("Took you " + str(tries) + " tries tho!")
