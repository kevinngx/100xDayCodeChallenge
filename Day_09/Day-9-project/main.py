from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

# 1. Show Logo
print(art.logo)
bids = {}

# 2. Ask for name

def get_response(bids):

  name = input("What is your name? ")

  # 3. Ask for Bid Price
  bids[name] = int(input("What is your bid? "))

  # 4. Ask if there are any other bidders, and call function again
  if(input("Are there any other bidders? ").lower() == "yes" ):
    clear()
    print(art.logo)
    get_response(bids)

# Call the function
get_response(bids)
#print(bids)

# 5. Find the highest bidder and print result
max_key = ""
max_bid = 0

for key in bids:
  if bids[key] > max_bid:
    max_bid = bids[key]
    max_key = key

clear()
print(f'The winner is {max_key} and their bid was ${max_bid}')