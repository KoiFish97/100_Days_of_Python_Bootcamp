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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("During your search you come across a group of pirates and are forced to flee.")
left_right = input("At the fork, do you go Left or Right? ")
if (left_right == "Left") or (left_right == "left"):
    print("You come to a dock. You can either swim across or wait in a narrow alley behind you and hope they run past.")
    swim_wait = input("Swim or Wait? ")
    if (swim_wait == "Wait") or (swim_wait == "wait"):
        print("After waiting for the pirates to run past, you burst into a room full of colored doors.")
        door = input("Which colored door do you choose to enter? ")
        if (door == "Purple") or (door == "purple"):
            print("You found the treasure!! Enjoy your Puzzle Box :P")
        elif (door == "Red") or (door == "red"):
            print("You triggered a flamethrower trap and were burnt to a crisp. Game Over")
        elif (door == "Blue") or (door == "blue"):
            print("You released a giant cyclops. Seems he was hungry. Game Over")
        elif (door == "Yellow") or (door == "yellow"):
            print("Well that was a magnifying glass ceiling. You burst into flames. Game Over")
        elif (door == "Green") or (door == "green"):
            print("Those are gorgeous flowers. You were distracted long enough for the pirates to catch up. Game Over.")
    else:
        print("You were eaten by a shark just before you reached the other side. Unlucky. Game Over")
else:
    print("You ran right into a group of bandits. Game Over")
