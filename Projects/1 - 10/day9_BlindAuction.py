import day9_BlindAuctionArt
from os import system
# Show logo
print(day9_BlindAuctionArt.logo)
print("Welcome to the secret auction program.")

auction_bids = {}

# Add name and bid into a dictionary and the key and value
def add_to_dictionary(bidder_name, bid_value):
    auction_bids.update({bidder_name : bid_value})

def name_and_bid():
    # Ask user for name
    name = input("What is your name?: ")
    # Ask user for bid price
    bid = int(input("What's your bid?: $"))
    add_to_dictionary(name, bid)

# Clear the screen so next user can't see previous bids
def clear_screen():
    system('cls')

# Find the highest bidder and declare them the winner
def winning_bid():
    highest_bid = 0
    winner = ""
    for name in auction_bids:
        if auction_bids[name] > highest_bid:
            highest_bid = auction_bids[name]
    for name, bid in auction_bids.items():
        if bid == highest_bid:
            winner = name
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


# Get name and bid for the first time
name_and_bid()

next_bidder = True
while next_bidder == True:
    # Ask if there are other users who want to bid
    any_others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if any_others == "yes":
        # If yes, clear screen and start from name
        clear_screen()
        name_and_bid()
    else:
        next_bidder = False
        clear_screen()
        winning_bid()
        # If no, find the highest bid in the dictionary and declare them the winner
