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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
game_image = [rock, paper, scissors]
image_names = ["Rock", "Paper", "Scissors"]

# User choice greater than 3 or less than 0 needs to be invalid
if user_choice >= 3 or user_choice < 0:
    print("Invalid number. Please pick 0 for Rock, 1 for Paper, 2 for Scissors.")

else:
    print(game_image[user_choice])
    print(f"You have chosen {image_names[user_choice]}.")

    print(game_image[computer_choice])
    print(f"Your opponent has chosen {image_names[computer_choice]}.")
# check if computer chose 0 and user chose 2 (Rock beats scissors)
    if computer_choice == 0 and user_choice == 2:
        print(f"{image_names[computer_choice]} beats {image_names[user_choice]}. You Lose.")
# check if user chose 0 and computer chose 2 (Rock beats scissors)
    elif user_choice == 0 and computer_choice == 2:
        print(f"{image_names[user_choice]} beats {image_names[computer_choice]}. You Win!!")
# with 0 and 2 covered should just need to check if choice is greater than (user 1 computer 0 or user 1 computer 2)
# check if computer > user
    elif computer_choice > user_choice:
        print(f"{image_names[computer_choice]} beats {image_names[user_choice]}. You Lose.")
# check if user > computer
    elif user_choice > computer_choice:
        print(f"{image_names[user_choice]} beats {image_names[computer_choice]}. You Win!!")
# check if both user input and computer are ==
    elif user_choice == computer_choice:
        print(f"Both you and your opponent chose {image_names[user_choice]}. It's a draw.")
