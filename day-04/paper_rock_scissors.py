import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose?")
player_choice = input("Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
computer_choice = random.randint(0, 2)

print(player_choice)
print(computer_choice)
