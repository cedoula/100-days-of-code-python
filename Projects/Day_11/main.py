from art import logo
import random

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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(hand):
  hand.append(random.choice(cards))
  return hand

def handle_ace(hand):
  if sum(hand) > 21 and 11 in hand:
    ace_index = hand.index(11)
    hand[ace_index] = 1
  return hand

def play_blackjack():
  continue_game = True
  user_wants_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if user_wants_play == 'y':
    clear()
    print(logo)

    user_hand = []
    computer_hand = []

    #Deal 2 cards for the user and 2 cards for the computer
    for _ in range(2):
      deal_card(user_hand)
      deal_card(computer_hand)

    handle_ace(user_hand)
    handle_ace(computer_hand)

    #If you or Computer have a natural Blackjack
    if sum(user_hand) == 21 or sum(computer_hand) == 21:
      if sum(user_hand) == 21:
        print(f'    Your cards: {user_hand}, current score: 0')
        print(f'    Computer\'s first card: {computer_hand[0]}')
        print(f'    Your final hand: {user_hand}, final score: 0')
        while sum(computer_hand) < 17:
          deal_card(computer_hand)
          handle_ace(computer_hand)

        print(f'    Computer\'s final hand: {computer_hand}, final score: {sum(computer_hand)}')
        if sum(computer_hand) == 21:
          print("It's a tie. 🙃")
          play_blackjack()
        else:
          print("You win with a natural Blackjack! 🙌")
          play_blackjack()
      else:
        print(f'    Your cards: {user_hand}, current score: {sum(user_hand)}')
        print(f'    Computer\'s first card: {computer_hand[0]}')
        print(f'    Your final hand: {user_hand}, final score: {sum(user_hand)}')
        print(f'    Computer\'s final hand: {computer_hand}, final score: 0')
        print("You lose! Your opponent has a natural Blackjack. 😢")
        play_blackjack()
    #If no natural blackjack
    else:
      print(f'    Your cards: {user_hand}, current score: {sum(user_hand)}')
      print(f'    Computer\'s first card: {computer_hand[0]}')
      draw = input("Type 'y' to get another card, type 'n' to pass: ")

      while draw == 'y':
        deal_card(user_hand)
        handle_ace(user_hand)
        print(f'    Your cards: {user_hand}, current score: {sum(user_hand)}')
        print(f'    Computer\'s first card: {computer_hand[0]}')
        if sum(user_hand) > 21:
          print(f'    Your final hand: {user_hand}, final score: {sum(user_hand)}')
          while sum(computer_hand) < 17:
            deal_card(computer_hand)
            handle_ace(computer_hand)
          print(f'    Computer\'s final hand: {computer_hand}, final score: {sum(computer_hand)}')
          print("Bust! You lose. 🤬")
          draw = 'n'
          continue_game = False
          play_blackjack()
        else:
          draw = input("Type 'y' to get another card, type 'n' to pass: ")
      
      if continue_game:
        print(f'    Your final hand: {user_hand}, final score: {sum(user_hand)}')
        while sum(computer_hand) < 17:
          deal_card(computer_hand)
          handle_ace(computer_hand)
        print(f'    Computer\'s final hand: {computer_hand}, final score: {sum(computer_hand)}')

        if sum(computer_hand) > 21:
          print("Your opponent has busted. You win! 😁")
          play_blackjack()
        else:
          if sum(user_hand) == sum(computer_hand):
            print("It's a tie. 🙃")
            play_blackjack()
          elif sum(user_hand) == 21:
            print("You win. 😁")
            play_blackjack()
          elif sum(computer_hand) == 21:
            print("You lose! 😢")
            play_blackjack()
          else:
            if sum(user_hand) > sum(computer_hand):
              print("You win! 😁")
              play_blackjack()
            else:
              print("You lose. 😢")
              play_blackjack()
  else:
    print("Bye! See you next time. 👋")

play_blackjack()