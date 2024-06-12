# Conditionals

# if condition:
#   do this
# else
#   do this

# water_level = 50
# if water_level > 80:
#     print("Drain Water")
# else:
#     print("Continue")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# if height >= 120:
#     print("You can ride the rollercoaster!!")
# else:
#     print("You are not tall enough to ride the rollercoaster :(")

# Nested if / else
# if condition:
#     if condition:
#         do this
#     else:
#         do this
# else:
#     do this

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# age = int(input("How old are you?"))
# if height >= 120:
#     if age < 12:
#         print("Your ticket costs $5")
#     elif age <= 18:
#         print("Your ticket costs $7")
#     else:
#         print("Your ticket costs $12")
# else:
#     print("You are not tall enough to ride this rollercoaster :(")

# Multiple If Statements in Succession
# if condition1:
#   do this
# if condition2:
#   do this
# if condition3:
#   do this

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride this rollercoaster!!")
#     age = int(input("How old are you? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets cost $8.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets cost $7.")
#     else:
#         bill = 12
#         print("Adult tickets cost $12.")
#     wants_photo = input("Do you want a photo taken? Y or N? ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}.")
# else:
#     print("You are not tall enough to ride this rollercoaster :(")

# Comparison Operators
# > Greater Than
# < Less Than
# >= Greater Than or Equal
# <= Less Than or Equal
# == Equal to
# != Not equal to

# Logical Operators
# A and B - If A or B are False the condition is False
# C or D - Condition needs 1 or the other
# not E

# a = 12

# a > 15 - False
# a > 10 - True
# a > 10 and a < 13 - True
# a > 15 and < 13 - False
# not a > 15 - True

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride this rollercoaster!!")
#     age = int(input("How old are you? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets cost $8.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets cost $7.")
#     elif age >= 45 and age <= 55:
#         print("Your ticket is free!!")
#     else:
#         bill = 12
#         print("Adult tickets cost $12.")
#     wants_photo = input("Do you want a photo taken? Y or N? ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}.")
# else:
#     print("You are not tall enough to ride this rollercoaster :(")

# Modulo
# % used to give the remainder after division
# 6 / 2 = 3 with no remainder
# 6 % 2 = 0
# When used in code remember == for equal to

# Day 3 Odd or Even
# My Solution (Matched Challenge Solution)
# number = int(input())
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# Day 3 - BMI 2.0
# My Solution (Matches Challenge Solution)
# height in meters
# height = float(input())
# weight in kilograms
# weight = int(input())
# bmi = weight / height ** 2
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")

# Day 3 - Leap Year
# My Solution (Matches Challenge Solution)
# year = int(input())
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")

# Day 3 - Pizza Order Practice
# My Solution
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? S, M, or L
# add_pepperoni = input()  # Do you want pepperoni? Y or N
# extra_cheese = input()  # Do you want extra cheese? Y or N
# bill = 0

# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1

# elif size == "M":
#     bill = 20
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1

# elif size == "L":
#     bill = 25
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1

# print(f"Your final bill is: ${bill}.")

# Challenge Solution
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? "S", "M", or "L"
# add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
# extra_cheese = input()  # Do you want extra cheese? "Y" or "N"
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")


# Day 3 Love Calculator
# My Solution
# name1 = input()  # What is your name?
# name2 = input()  # What is their name?
# names = name1 + name2
# names = names.lower()
# t = names.count("t")
# r = names.count("r")
# u = names.count("u")
# l = names.count("l")
# o = names.count("o")
# v = names.count("v")
# e = names.count("e")
# true = t + r + u + e
# love = l + o + v + e
# true_love = f"{true}{love}"
# true_love = int(true_love)
# if (true_love < 10) or (true_love > 90):
#     print(f"Your score is {true_love}, you go together like coke and mentos.")
# elif (true_love >= 40) and (true_love <= 50):
#     print(f"Your score is {true_love}, you are alright together.")
# else:
#     print(f"Your score is {true_love}.")

# Challenge Solution
# print("The Love Calculator is calculating your score...")
# name1 = input()  # What is your name?
# name2 = input()  # What is their name?
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")
