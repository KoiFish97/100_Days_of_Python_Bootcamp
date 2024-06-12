# If the bill was $150.00 split between 5 people with a 12% tip.

# Each person should pay (150 / 5) * 1/12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

# 12% is 12 / 100 = 0.12
# 150 / 0.12 = 18.0
# 150 + 18 = 168
# Short version is 150 * 1.12
# 168.00 / 5 = 33.60

print("Welcome!!")
bill = float(input("How much is your bill?"))
tip = input("What tip do you want to give? 10, 12, or 15?")
people = input("How many people are splitting the bill?")

# print(bill, tip, people)

bill_and_tip = bill * (1 + int(tip) / 100)
# print(bill_and_tip)

final_cost = bill_and_tip / int(people)
# print(final_cost)

print(f"Each person should pay: ${final_cost:.2f}")