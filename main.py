# Angela Yu - 100 Days of Code - Day 9: Blind Auction Program
# This program simulates a blind auction where multiple bidders can place bids
# and the highest bidder is determined at the end

from art import logo  # Import ASCII art logo from external art module
print(logo)  # Display the auction logo at program start


def find_highest_bidder(bidding_record):
    """
    Function to determine the winner of the auction
    Takes a dictionary of bidders and their bids as input
    """
    highest_bid = 0  # Initialize highest bid tracker
    winner = ""      # Initialize winner name tracker
    
    # Loop through each bidder in the bidding record dictionary
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]  # Get the bid amount for current bidder
        
        # Check if current bid is higher than the previous highest
        if bid_amount > highest_bid:
            highest_bid = bid_amount  # Update highest bid
            winner = bidder           # Update winner name
    
    # Announce the winner and winning bid amount
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Main program execution
bids = {}  # Dictionary to store all bidder names and their corresponding bids
continue_bidding = True  # Flag to control the bidding loop

# Main bidding loop - continues until no more bidders
while continue_bidding:
    # Get bidder information
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))  # Convert input to integer
    
    # Store the bid in the dictionary with name as key and price as value
    bids[name] = price
    
    # Ask if there are more bidders
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    
    # Check user's response to determine next action
    if should_continue == "no":
        continue_bidding = False  # Exit the loop
        find_highest_bidder(bids)  # Determine and announce the winner
    elif should_continue == "yes":
        print("\n" * 20)  # Clear screen by printing 20 newlines (for privacy in blind auction)
        # Loop continues to accept next bidder