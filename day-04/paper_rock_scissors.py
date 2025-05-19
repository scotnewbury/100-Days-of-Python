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

game_images = [rock, paper, scissors]
print("What do you choose?")
player_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

if player_choice >= 0 and player_choice < 3:
    print(f"You chose: {game_images[player_choice]}")

print(f"Computer chose: {game_images[computer_choice]}")

if 0 <= player_choice <= 2:
    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 0 and computer_choice == 2) or \
            (player_choice == 1 and computer_choice == 0) or \
            (player_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
else:
    print("You entered an invalid number - you lose!")
