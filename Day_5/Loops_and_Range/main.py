# Range Function

# for number in range(a, b):
#     print(number)

# Prints 1 - 10. If 10 needs to be printed range needs to be 1 - 11
# for number in range(1, 10):
#     print(number)

# Extra number is the step. Skips 3 each number
# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# Day 5 - Adding Even Numbers

# My Answer
# target = int(input()) # Enter a number between 0 and 1000

# total = 0
# for number in range(2, target + 1, 2):
#   total += number
# print(total)

# Alternate Provided Answer
# alternative_sum = 0
# for number in range(1, target + 1):
#   if number % 2 == 0:
#     alternative_sum += number
# print(alternative_sum)

# Day - 5 FizzBuzz Game

# target = 100
# for number in range(1, target + 1):
#     if number % 15 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
