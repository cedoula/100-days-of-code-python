from turtle import Turtle
from random import uniform, choice

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed(1)
        self.seth(37)
        self.moving_distance = 2
    
    def move_ball(self):
        self.forward(self.moving_distance)

    def bounce_on_wall(self):
        self.seth(360 - self.heading())

    def bounce_on_r_paddle(self):
        self.seth(self.heading() + 90)

    def bounce_on_l_paddle(self):
        self.seth(self.heading() - 90)

    def reset_ball(self):
        if self.xcor() > 0:
            direction = uniform(127, 217)
        else:
            direction = choice([uniform(0, 37), uniform(323, 360)])
        self.goto(0,0)
        self.seth(direction)
        self.moving_distance = 2
        self.move_ball()

    def increase_ball_speed(self):
        self.moving_distance += 1