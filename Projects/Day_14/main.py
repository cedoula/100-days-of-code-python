import random
from art import logo, vs
from game_data import data
# import only system from os 
from os import system, name 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def game():
  continue_game = True
  couple = [random.choice(data), random.choice(data)]
  if couple[0] == couple[1]:
        couple[1] = random.choice(data)
  score = 0

  while continue_game:
    clear()
    print(logo)
    if score > 0:
      print(f"You're right! Current score: {score}.")
    print(f"Compare A: {couple[0]['name']}, a {couple[0]['description']}, from {couple[0]['country']}.")
    print(vs)
    print(f"Against B: {couple[1]['name']}, a {couple[1]['description']}, from {couple[1]['country']}.")
    pick = input("Who has more followers? Type 'A' or 'B': ").lower()

    if pick == 'a':
      user_choice = couple[0]
      against = couple[1]
    elif pick == 'b':
      user_choice = couple[1]
      against = couple[0]

    if user_choice['follower_count'] >= against['follower_count']:
      score += 1
      couple[0] = couple[1]
      couple[1] = random.choice(data)
      if couple[0] == couple[1]:
        couple[1] = random.choice(data)
    else:
      continue_game = False
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")

game()
