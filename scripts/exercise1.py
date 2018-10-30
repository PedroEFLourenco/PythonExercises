import datetime

name = input("Hi, what's your name? ")
age = int(input("How old are you? "))

currentyear = datetime.datetime.now().year
birthyear = currentyear - age

print("Glad to meet you " + name)
print("Did you know that you are going to turn 100 by " + str(birthyear + 100)
      + "?\n")
print("By the way, just to bore you to death, let me tell you how old you "
      "will be every year until you turn 100: \n")


while age < 100:
    age += 1
    print(name + ", by " + str(birthyear + age) + " you will be " +
          str(age) + " years old!")
