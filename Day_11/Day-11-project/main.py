
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
import art

# Deal cards using list of cards
def deal_card(cards):
  card = cards[random.randint(0, len(cards) - 1)]
  return card

# Calculate scores
def calculate_score(hand):
  score = 0
  ace_counter = 0
  # Sum Hand
  for card in hand:
    if card == 11:
      ace_counter += 1
    score += card

  # Check for blackjack
  if len(hand) == 2 and score == 21:
    return 0

  while score > 21 and ace_counter > 0:
    #Remove aces
    hand.remove(11)
    hand.append(1)
    ace_counter -= 1
    score -= 10

  return score

# Compare scores and print winner
def compareScore(a_name, a_hand, b_name, b_hand):
  a_score = calculate_score(a_hand) 
  b_score = calculate_score(b_hand)

  if (a_score > 21):
    print(f"{b_name} wins with a score of {b_score}")
  elif (b_score > 21):
    print(f"{a_name} wins with a score of {a_score}")
  elif (a_score > b_score):
    print(f"{a_name} wins with a score of {a_score}")
  elif (b_score > a_score):
    print(f"{b_name} wins with a score of {b_score}")
  else:
    print("It's a tie!")

# Card list
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_game():
  # 1. Show art
  print(art.logo)

  # 2. Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = [deal_card(cards), deal_card(cards)]
  dealer_cards = [deal_card(cards), deal_card(cards)]

  print(f"Your hand is {user_cards} with a score of {calculate_score(user_cards)}")
  print(f"The dealer's hand is {dealer_cards} with a score of {calculate_score(dealer_cards)}")

  # 3. Draw additional cards
  if calculate_score(user_cards) != 21 or calculate_score(dealer_cards) != 21:
    
    while (calculate_score(user_cards) < 21) and (input("\ndo you want to draw another card (y/n) ") == "y") :
      new_card = deal_card(cards)
      user_cards.append(new_card)
      print(f"You have drawn a {new_card}")
      print(f"Your hand is now {user_cards} with a score of {calculate_score(user_cards)}")
      
      # Dealer's hits - note: if the user busts then we skip the dealer's draw phase
      while calculate_score(dealer_cards) < 17 and calculate_score(user_cards) <= 21:
        dealer_cards.append(deal_card(cards))

  # 4. Print results
  print("\nResults:")
  print(f"Your hand is {user_cards} with a score of {calculate_score(user_cards)}")
  print(f"The dealer's hand is {dealer_cards} with a score of {calculate_score(dealer_cards)}")

  # 5. Announce winners
  compareScore("Player", user_cards, "Dealer", dealer_cards)


# Start of program execution

repeat = "y"
while repeat == "y":
  play_game()
  repeat = input("\nWould you like to play another game? ")
print("Thank you for playing!")