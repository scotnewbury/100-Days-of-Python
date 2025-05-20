import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level
# my_password = ""
# for letter in range(1, nr_letters + 1):
#     my_password += random.choice(letters)
# for symbol in range(1, nr_symbols + 1):
#     my_password += random.choice(symbols)
# for number in range(1, nr_numbers + 1):
#     my_password += random.choice(numbers)

# print(my_password)

# Hard Level version 1
# password_length = int(nr_letters + nr_numbers + nr_symbols)
# print(password_length)
# my_password = ""

# for password_character in range(1, password_length + 1):
#     character_type = random.randint(1, 3)
#     if character_type == 1 and nr_letters > 0:
#         my_password += random.choice(letters)
#         print(my_password)
#         nr_letters -= 1
#     elif character_type == 2 and nr_symbols > 0:
#         my_password += random.choice(symbols)
#         print(my_password)
#         nr_symbols -= 1
#     elif character_type == 3 and nr_numbers > 0:
#         my_password += random.choice(numbers)
#         print(my_password)
#         nr_numbers -= 1

# Hard version 2
# Version 1 worked but the hint suggest shuffle

my_password = ""

for letter in range(0, nr_letters):
    my_password += random.choice(letters)
for symbol in range(0, nr_symbols):
    my_password += random.choice(symbols)
for number in range(0, nr_numbers):
    my_password += random.choice(numbers)

# We have all the characters in a single string
# Let's turn them into a list
char_list = list(my_password)

# Now we shuffle the characters
random.shuffle(char_list)

# Now we put it back together as a string
my_password = "".join(char_list)

# Print the final password
print(my_password)

# Angela dropped everyting into a list, shuffled it,
# then she used a for loop to build the string
