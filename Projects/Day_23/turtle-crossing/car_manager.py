from turtle import Turtle
from random import choice, uniform

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1,2,1)
        self.color(choice(COLORS))
        self.goto(310, uniform(-240,240))
        self.seth(180)
        self.speed("slowest")
        self.moving_rate = move_distance

    def move(self):
        self.forward(self.moving_rate)

    def speed_up(self):
        self.moving_rate += MOVE_INCREMENT
        