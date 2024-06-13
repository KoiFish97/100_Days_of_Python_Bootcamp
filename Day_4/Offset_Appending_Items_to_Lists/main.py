# Lists
# Grouped data instead of singular variables

# fruits = ["cherry", "banana"]


states_of_america = ["Delaware", "California", "Nevada", "Arizona"]
# starts at beginning of list
# print(states_of_america[2])
# starts at end of list
# print(states_of_america[-1])

# edit list item
# states_of_america[2] = "Utah"
# print(states_of_america[2])

# add item to end of list
# states_of_america.append("Ohio")
# print(states_of_america)

# extend a list
# states_of_america.extend(["Utah", "Ohio", "Washington", "New York"])
# print(states_of_america)

# print amount of items in a list
# print(len(states_of_america))

# Nested lists
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines" "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# two lists in 1 list
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)


# Day 4 - Banker roulette
# input info is done behind the scenes in challenge
# name_count = len(names)

# who_pays = random.randint(0, name_count - 1)
# print(names[who_pays] + " is going to buy the meal today!")

# Day 4 - Treasure Map
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# Get letter from input
# letter = position[0].lower()
# make a letter list
# horizontal_pos = ["a", "b", "c"]
# index where the letter is in the list
# letter_index = horizontal_pos.index(letter)
# print(letter_index)
# index where number is in the list
# number_index = int(position[1]) - 1
# print(number_index)
# map[number_index][letter_index] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")
