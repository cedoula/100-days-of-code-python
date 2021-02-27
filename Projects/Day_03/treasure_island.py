print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


#Where do you want to go
direction = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")
if direction.lower() == "right": print("Oh no! You've fell into the hidden hole. Game Over!")
elif direction.lower() == "left":
  #What do you do
  action = input("You've arrived at a lake. There is an island in the middle of the lake.\nType 'swim' to swim across or type 'wait' to wait for a boat.\n")
  if action.lower() == "swim": print("Oh no! You've been eaten by a great white shark. Game Over!")
  elif action.lower() == "wait":
    #Which door?
    door = input("You arrive on the island. There is a house with 3 doors. One red, one yellow and one blue.\nWhich one do you choose?\n")
    if door.lower() == "yellow": print("Oh Great! You've found Blackbeard's Treasure. You win!")
    elif door.lower() == 'red' or door.lower() == 'blue': print("Oh no! You've been captured by Blackbeard and his crew. Game Over!")
    else: print("Wrong choice! Try the game again.")
  else: print("Wrong choice! Try the game again.")
else: print("Wrong choice! Try the game again.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload