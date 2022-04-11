from art import logo
print(logo)

print("Welcome to the secret auction program.")

bids = {}
bid_process = True


def compare(bidding_record):
  max_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = int(bidding_record[bidder])
    if bid_amount > max_bid:
      max_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner}, with a bid of ${max_bid}")    
while bid_process:
  name = input("What is your name?: ")
  bid_amount = input("What is your bid? $")
  bids[name] = bid_amount
  other_bid = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
  if other_bid == "yes":
  
    bid_process = True
  if other_bid == "no":
    
    bid_process = False
    compare(bidding_record = bids)