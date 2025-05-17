# Lesson 22
# Conditional statements
# if/else

# print("Welcome to the rolloercoaster!")

# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can buy a ticket")
# else:
#     print("Sorry you can't ride")

# Lesson 23 - Modulo
# Take as input from a user, an number, cast it as an integer
# and determine if it's odd or even
# If it's odd, print "Odd" otherwise print "Even"

# number = int(input("Please enter a number: "))

# if number % 2:    # Using the remainder without evaluation
#     print("Odd")    # The modulo result was 1 so the number is odd
# else:
#     print("Even")   # The modulo result was 0 so the number if even

# Lesson 24 - nested if statments and elif statements

# print("Welcome to the rolloercoaster!")

# height = int(input("What is your height in cm? "))
# age = int(input("How old are you? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     if age < 12:
#         print("Your ticket price is $5")
#     elif age <= 18:
#         print("Your tickket price is $7")
#     else:
#         print("Your ticket price is $12")
# else:
#     print("Sorry you can't ride")

# Lesson 25 Multiple if Statements in Succession
print("Welcome to the rolloercoaster!")

height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
ticket_total = 0  # initialize ticket total

if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        print("Child tickets are $5.")
        ticket_total += 5
    elif age <= 18:
        print("Youth tickets are $7.")
        ticket_total += 7
    else:
        print("Adult tickets are $12.")
        ticket_total += 12
    wants_photo = input("Would you like a photo? Type 'y' for Yes and 'n' for No.")
    if wants_photo == 'y':
        ticket_total += 3
    print(f"Your total ticket price is: ${ticket_total}")
else:
    print("Sorry you can't ride")
