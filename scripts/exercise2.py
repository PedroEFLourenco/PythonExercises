number1 = input("Yo, Say a number: ")

restOfDiv = int(number1) % 2

if (int(number1) % 2 == 0):
    print("Bruh, that shit's even as f*** !")
else:
    print("Do you even even?")

print("Let's try something new, mate!")
number2 = input("Give me a number, I'll tell you if it is a multiple of 4: ")

if (int(number2) % 4 == 0):
    print("You got the hang of this, " + str(number2) + " is definitely a\
multiple of 4")
else:
    print("Does that look like a multiple of 4? You dense M....")

print("Let's try another something new, mate!\n")
print("You'lll give me two numbers, I'll tell you if the first divides evenly \
with the second!")
number3 = input("Give me a number: ")
number4 = input("Give me another number: ")

if (int(number3) % int(number4) == 0):
    print("Yo, " + str(number3) + " does divide evenly by " + str(number4) +
          " !")
else:
    print("Nah man, that ain't even!")
