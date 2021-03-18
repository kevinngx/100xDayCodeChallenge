
import art
import game_data
import random

print(art.logo)

player_score = 0
game_continue = True
while (game_continue == True):
  
  # Get two random options
  print("----------------------------------------------------------------------------")
  player_a = game_data.data[random.randint(0, len(game_data.data))]
  player_b = game_data.data[random.randint(0, len(game_data.data))]

  # Get answer 
  if(player_a["follower_count"] > player_b["follower_count"]):
    correct_answer = "a"
  else:
    correct_answer = "b"

  # Present question and get input
  print('Compare A: ' + player_a['name'] + " a " + player_a['description'] + ", from " + player_a['country'])
  print(art.vs)
  print('Compare B: ' + player_b['name'] + " a " + player_b['description'] + ", from " + player_b['country'])
  answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()
 
  # Check answer
  if answer == correct_answer:
    player_score += 1
  else:
    print("\nSorry, that's wrong. Final score: " + str(player_score))
    game_continue = False
    break