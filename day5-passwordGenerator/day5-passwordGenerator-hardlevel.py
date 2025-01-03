import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard level 
mypassword_list = []
for val in range(1, nr_letters+1):
    mypassword_list.append(random.choice(letters))
for val in range(1, nr_symbols+1):
    mypassword_list.append(random.choice(symbols))
for val in range(1, nr_numbers+1):
    mypassword_list.append(random.choice(numbers))
print(mypassword_list)
random.shuffle(mypassword_list)
print(mypassword_list)

passwd = ""
for char in mypassword_list:
    passwd += char
print(passwd)


#
# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 5
# How many symbols would you like?
# 3
# How many numbers would you like?
# 2
# ['H', 'f', 'j', 'w', 'H', '#', '&', '$', '0', '2']
# ['#', '$', 'H', 'H', '&', 'w', '2', 'f', 'j', '0']
# #$HH&w2fj0


