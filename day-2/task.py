# Day is focused on data types and manipulation of them
# len("hello")

# Print the first character of a string
# Subscripting

# print("Hello"[0])

# String
# print("123" + "345")

# Integer = whole number

 # Fix so that len will work with the numbers
# len("12345")

# type will show us the 'type' of a give value or variable
# print out all four data types to date - one per line
# print(type("name"))
# print(type(123))
# print(type(123.0))
# print(type(True))

# Type casting / conversion
# print("123" + "456") # concatinates the strings
# print(int("123") + int("456")) # casts the strings to integers, adds the numbers

# Correct line of code so it prints the number of letters in the name entered
# print("Number of letters in your name: " + len(input("Enter your name: ")))
#
# Looking at the line of code before running it, len() is being used on a string not a number, 
# will need to cast the input for it to work.

print("Number of letters in your name: " + str(len(input("Enter your name: "))))