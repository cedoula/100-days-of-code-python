from turtle import Turtle, Screen
import random


def go_to_starting_line(list_turtles):
    for i in range(len(list_turtles)):
        list_turtles[i].goto(x=-230, y=-125 + 50 * i)

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#Create list of Turtle instances
turtles = [Turtle(shape="turtle") for color in colors]
#Apply color and penup
for turtle in turtles:
    turtle.color(colors[turtles.index(turtle)])
    turtle.penup()
go_to_starting_line(turtles)

if user_bet:
    is_race_on= True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"'You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




# tim.penup()
# tim.goto(x=-230, y=-100)
# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def turn_left():
#     tim.seth(tim.heading() - 10)
# def turn_right():
#     tim.seth(tim.heading() + 10)
# def clear():
#     tim.clear()
#     tim.reset()

# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)

screen.exitonclick()