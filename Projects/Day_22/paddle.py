from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1,1)
        self.goto(side)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
    
    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)