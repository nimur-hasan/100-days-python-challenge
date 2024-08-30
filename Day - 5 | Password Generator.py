from random import random, choice, shuffle

alphabets = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
symbols = [
  '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
  '+', '[', ']', '{', '}', ';', ':', '"', "'", ',', '<', '.', '>',
  '/', '?', '\\', '|', '`', '~'
]
numbers = [
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
password_list = []

# nr_letters = 4
for char in range(0, nr_letters ):
  password_list.append(choice(alphabets))

for sym in range(0, nr_symbols):
  password_list.append(choice(symbols))

for num in range(0, nr_numbers):
  password_list.append(choice(numbers))

shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(password)
