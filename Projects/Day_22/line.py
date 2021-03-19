from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,-300)
        self.seth(90)
        while self.ycor() < 300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.hideturtle()