from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bids={}
a=False
def highest_bid(bidding_record):
  highest_bid=0
  winner=""
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"the winner is {winner} with a bid of ${highest_bid}")
while not a:
  print("welcome to the secret auction program")
  name=input("what is your name?")
  bid=int(input("what's your bid? $"))
  bidders=input("are there any other bidders. type yes' if yes and 'no' if no")
  bids[name]=bid
  if bidders=="no":
    a=True
    highest_bid(bids)
  elif bidders=="yes":
    clear()




    
  
