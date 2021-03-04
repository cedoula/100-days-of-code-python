alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  #Handle shifts above 26
  shift_amount = shift_amount % 26
  end_text = ""
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      if cipher_direction.lower() == 'encode':
        new_position = position + shift_amount
        if new_position > 25: new_position -= 26
      else:
        new_position = position - shift_amount
        if new_position < 0: new_position += 26
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

#Continue as long as the user say 'yes'
continue_game = True
while continue_game:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction.lower() != 'encode' and direction.lower() != 'decode':
    print("You have made a wrong choice. Please try again.")
    exit()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  user_decision = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if user_decision == 'no':
    print("Goodbye!")
    continue_game = False