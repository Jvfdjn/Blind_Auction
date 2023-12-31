import os

# Clear terminal function
def clear_terminal():
    # Check the operating system and clear the terminal accordingly
    os.system('cls' if os.name == 'nt' else 'clear')

# Import ASCII art from the 'art_of_bid' module
from art_of_bid import art
print(art)

# Dictionary to store bids
bids = {}

# Flag to check if bidding is finished
bidding_finished = False

# Function to find the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # Iterate through the bidding records to find the highest bid and winner
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    # Print the winner and their bid
    print(f"The winner is {winner} with a bid of Rs.{highest_bid}")

# Main bidding loop
while not bidding_finished:
    # Get bidder's name
    names = input("What is your name? ")
    
    # Get bidding price from the bidder
    price = int(input("Enter your bidding price. Rs."))
    
    # Store the bid in the dictionary
    bids[names] = price 
    
    # Check if there are any other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    
    # If there are no more bidders, finish the bidding and find the winner
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    
    # If there are more bidders, clear the terminal for the next bidder
    elif should_continue == "yes":
        clear_terminal()
