import random
from hangman_words import word_list
from hangman_art import logo, stages
import os


def clear():
    os.system('cls')


end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# Print Logo
print(logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
guesses = []
for _ in range(word_length):
    display += "_"

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    clear()

    # Check if guessed letter has been guessed before
    if guess in guesses:
        print(f"You've already guessed {guess}.")
    else:
        guesses.append(guess)

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        # If guess is not a letter in the chosen_word,
        # Then reduce 'lives' by 1.
        # If lives goes down to 0 then the game should stop and, it should print "You lose."

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            # print(lives)
        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
        elif lives == 0:
            end_of_game = True
            print("You Lose")

        print(stages[lives])
