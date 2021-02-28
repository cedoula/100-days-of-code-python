import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock Paper Scissors Game!")
#Prompt user to make a choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#If wrong input from the user, stop the program
if user_choice not in range(3): 
  print("You have typed an invalid number. Restart.")
else:
  #Build rock paper scissors list
  rock_paper_scissors_list = [rock, paper, scissors]

  #Print user and computer choices
  user_rps = rock_paper_scissors_list[user_choice]
  comp_rps = random.choice(rock_paper_scissors_list)
  print(f'{user_rps}\n\nComputer chose:\n\n{comp_rps}\n')

  #Determine who wins
  if user_rps == comp_rps:
    print("It is a draw.")
  else:
    if user_rps == rock and comp_rps == scissors: 
      print("You win! :-)")
    if user_rps == rock and comp_rps == paper: 
      print("You lose. :-(")
    if user_rps == paper and comp_rps == rock: 
      print("You win! :-)")
    if user_rps == paper and comp_rps == scissors: 
      print("You lose. :-(")
    if user_rps == scissors and comp_rps == paper: 
      print("You win! :-)")
    if user_rps == scissors and comp_rps == rock: 
      print("You lose. :-(")