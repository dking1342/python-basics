import random

print("Password Generator")
print("==================")

chars = "1234567890)(*&^%$#@!qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
number = int(input("enter amount of passwords (enter a number) "))
length = int(input("enter a password length (enter a number "))

print("\nhere are your passwords: ")

for passwords in range(number):
    pw = ""
    for index in range(length):
        pw += random.choice(chars)
    print(pw)

