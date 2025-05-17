# total_pizza_cost = 0  # Set and initialize variable

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# if size == "s":
#     total_pizza_cost += 15
#     if pepperoni == "y":
#         total_pizza_cost += 2
# elif size == "m":
#     total_pizza_cost += 20
#     if pepperoni == "y":
#         total_pizza_cost += 3
# else:
#     total_pizza_cost += 25
#     if pepperoni == "y":
#         total_pizza_cost += 3

# if extra_cheese == "y":
#     total_pizza_cost += 1

# print(f"Your final bill is: ${total_pizza_cost}")

#
# Code was modified to pass automated tests as follows
# 1. Missed period at end of output statement
# 2. Tests were written using uppercase input, had to match to pass

total_pizza_cost = 0  # Set and initialize variable

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    total_pizza_cost += 15
    if pepperoni == "Y":
        total_pizza_cost += 2
elif size == "M":
    total_pizza_cost += 20
    if pepperoni == "Y":
        total_pizza_cost += 3
else:
    total_pizza_cost += 25
    if pepperoni == "Y":
        total_pizza_cost += 3

# Revision: move pepperoni check out
# Makes the code "dry"

if pepperoni == "Y":
    if size == "S":
        total_pizza_cost += 2
    else:
        total_pizza_cost += 3

if extra_cheese == "Y":
    total_pizza_cost += 1

print(f"Your final bill is: ${total_pizza_cost}.")
