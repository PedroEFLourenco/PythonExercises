''' My solution '''

eventualPalindrome = str(input("Give me a String so I can validate if it is a \
Palindrome: "))

i = 0
paliFlag = True
length = len(eventualPalindrome)

while(i < (length/2)):
    if eventualPalindrome[i] != eventualPalindrome[length-1-i]:
        print("Not a Palindrome")
        paliFlag = False
        break
    print(i)
    i += 1


if paliFlag:
    print("It is a Palindrome")

'''Solution from exercise solutions - Actually more elegant than mine'''

wrd = input("Please enter a word")
wrd = str(wrd)
rvs = wrd[::-1]  # Reversing the string with string[start_index:end_index:step]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
