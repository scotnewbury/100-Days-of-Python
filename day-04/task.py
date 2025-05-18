# Module 31 - Randomization

import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# Heads or Tails
# Create the code to randomly generate heads or tails

# Genereatea random number, 0 or 1
# 0 will be heads
# 1 will be tails

heads = 0
tails = 0

for i in range(1000):
    coin_flip = random.randint(0, 1)
    if coin_flip == 0:
        # print("Heads")
        heads += 1
    else:
        # print("Tails")
        tails += 1

print("I flipped the coin 100 times and here's what I got:")
print(f"The number of times heads came up: {heads}")
print(f"The number of times tails came up: {tails}")
