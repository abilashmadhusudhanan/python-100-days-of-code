from replit import clear
from logo import logo

bidders_available = "yes"
bidders_bids = dict()
max_bid = 0
max_bidder = ""

while bidders_available == "yes":
    clear()
    print(logo)
    print("")
    name = input("Name of the bidder: ")
    bid = int(input("Bid value: "))

    bidders_bids[name] = bid

    bidders_available = input("Is any other bidder available next (yes or no)? ")

clear()

for bidder in bidders_bids:
    if bidders_bids[bidder] > max_bid:
        max_bid = bidders_bids[bidder]
        max_bidder = bidder

print(f"The winner is {max_bidder} with the bid value of {max_bid}")