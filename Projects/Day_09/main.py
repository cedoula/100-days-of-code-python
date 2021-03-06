# import only system from os 
from os import system, name

#Define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

from art import logo

print(logo)
print("Welcome to the secret auction program.")


bids = {}
continue_bidding = True

while continue_bidding:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bids[name] = bid

  more = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if more.lower() == 'yes':
    clear()
  else:
    continue_bidding = False
    clear()
    max_bidder = max(bids, key = bids.get) 
    print(f'The winner is {max_bidder} with a bid of ${bids[max_bidder]}.')
