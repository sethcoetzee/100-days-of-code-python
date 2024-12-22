# Day 5 Project: Password Generator

import random

# initialise the lists of letters, numebrs, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# obtain the number of letters, symbols, and numbers from the user
print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

# generate the password by randomly selecting letters, symbols, and numbers, accoridng to the user's input
password = ""
for i in range(num_letters):
    password += random.choice(letters)

for i in range(num_symbols):
    password += random.choice(symbols)
    
for i in range(num_numbers):    
    password += random.choice(numbers)

# give the user their password (easy mode)
print("# Easy mode")
print(f"Your password is: {password}")

# turn the password string into a list
password_list = list(password)

# shuffle the order of the characters in the password
random.shuffle(password_list)

# turn the list back into a string
hard_password = ""
for char in password_list:
    hard_password += char

# give the user their password (hard mode)
print("# Hard mode")
print(f"Your password is: {hard_password}")