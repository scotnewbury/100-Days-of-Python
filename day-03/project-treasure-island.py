print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."  ` . "-._ _______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are standing at a fork in the road.")
fork_direction = input("Will you go left or right? ")

print(fork_direction)

if fork_direction != "left":
    print("Oh no! You didn't see the dragon waiting for you!")
    print("You've been burned to a crisp!")
    print("YOU LOSE! GAME OVER")
else:
    print("You come to a lake and can see a island in the distance.")
    swim_or_not = input("Will you swim or wait for a boat? ")
    if swim_or_not == "swim":
        print("Oops, did you forget you were wearing armor?")
        print("You've drowned!")
        print("YOU LOSE! GAME OVER")
    else:
        print("You arrive at the island and find a house with three doors.")
        print("The doors are each a different color, red, yellow, blue.")
        door_selection = input("Which door will you pick? ")
        if door_selection == "red":
            print("A demon reaches out through the flames and drags you into hell!")
            print("YOU LOSE! GAME OVER")
        elif door_selection == "blue":
            print("A bolt of lightning streaks out of the doorway, striking you dead!")
            print("YOU LOSE! GAME OVER")
        else:
            print("A ray of sunshine comes from the doorway and you see a kindly old man.")
            print("The old man smiles at you and say . . . .")
            print("\nYou have choosen wisely and won! CONGRATULATIONS!")
