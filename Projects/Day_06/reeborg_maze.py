#This code is to play the Reeborg 'Maze' game on https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()

    if not wall_in_front():
        move()
    else:
        if not wall_on_right():
            turn_right()    
        else:
            turn_left()    