from turtle import Turtle
from random import choice

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.seth(90)
        self.color(choice(COLORS))
        self.go_to_start_line()

    def move(self):
        self.forward(MOVE_DISTANCE)
    def go_to_start_line(self):
        self.goto(STARTING_POSITION)

    def reached_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y
            
            