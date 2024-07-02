from art import logo
import os

print(logo)
print("Welcome to The Secret Auction")

secret_auction = []


def clear():
    os.system('cls')


def add_bidder(user_name, user_bid):
    bids = {}
    bids["name"] = name
    bids["bid"] = bid
    secret_auction.append(bids)
    # print(secret_auction)


should_continue = True
while should_continue:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    add_bidder(user_name=name, user_bid=bid)

    while True:
        result = input("Is there another bidder?\n").lower()
        if result == 'no':
            should_continue = False
            break
        elif result == 'yes':
            break
        else:
            print("Invalid Input. Please enter 'Yes' or 'No'")
    clear()


highest_bid = 0
for bids in secret_auction:
    if bids["bid"] >= highest_bid:
        highest_bid = bids["bid"]
    # print(highest_bid)

for bids in secret_auction:
    if bids["bid"] == highest_bid:
        highest_bidder = bids["name"]
print(f'{highest_bidder} is the highest bidder')



