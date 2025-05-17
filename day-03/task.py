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

number = int(input("Please enter a number: "))

if number % 2:    # Using the remainder without evaluation
    print("Odd")    # The modulo result was 1 so the number is odd
else:
    print("Even")   # The modulo result was 0 so the number if even
