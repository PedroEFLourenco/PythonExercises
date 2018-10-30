a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
number = input("Say a number for me to use here: ")

for x in a:
    if (x < 5):
        b.append(x)


print(*b)

for x in a:
    if (x < int(number)):
        print(x)
