import random
from art import logo

#Global Constants
LIVES_EASY = 10
LIVES_HARD = 5
#Global var
lives = 0

def check_answer(myst_number, guess, lives):
  """Check mystery number against guess and returns the number of lives left."""
  if guess == myst_number:
    print(f"You got it! The answer was {myst_number}.")
  elif guess > myst_number:
    print("Too high.")
    return lives - 1
  else:
    print("Too low.")
    return lives - 1

def set_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return LIVES_EASY
  elif level == 'hard':
    return LIVES_HARD
  else:
    print("Wrong choice. Restart.")
    exit()

def game():
  print(logo)
  print("Welcome to the Mystery Number Game!\nI'm thinking of a number between 1 and 100.")
  mystery_number = random.randint(1,100)

  lives = set_level()

  user_guess = 0

  while user_guess != mystery_number and lives !=0:
    print(f'You have {lives} attemps remaining to guess the number.')
    user_guess = int(input("Make a guess: "))
    lives = check_answer(mystery_number, user_guess, lives)
    if user_guess != mystery_number:
      print("Guess again.")

  if lives == 0:
    print("You've run out of guesses. You lose.")

game()