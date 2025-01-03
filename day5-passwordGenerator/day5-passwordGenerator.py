import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level
mypassword = ""
for val in range(1, nr_letters+1):
    mypassword += letters[random.randint(1, len(letters))]
for val in range(1, nr_symbols+1):
    mypassword += symbols[random.randint(1, len(symbols))]
for val in range(1, nr_numbers+1):
    mypassword += numbers[random.randint(1, len(numbers))]
print(mypassword)

#Easy level - #2
mypassword = ""
for val in range(1, nr_letters+1):
    mypassword += random.choice(letters)
for val in range(1, nr_symbols+1):
    mypassword += random.choice(symbols)
for val in range(1, nr_numbers+1):
    mypassword += random.choice(numbers)
print(mypassword)

#
# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 5
# How many symbols would you like?
# 2
# How many numbers would you like?
# 3
# vQChN#*347
# Vcvwc#%582
