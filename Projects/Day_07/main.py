import random
from hangman_art import stages, logo
from hangman_words import word_list
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

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Create blanks
display = ["_" for letter in chosen_word]

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #Clear the screen
    clear()

    if guess in display:
      print(f'You\'ve already guessed {guess}')
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])