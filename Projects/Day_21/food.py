from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SHAPE = ["turtle", "circle", "triangle"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.shape(random.choice(SHAPE))
        self.color(random.choice(COLORS))
        self.goto(random.randint(-280,280), random.randint(-280,280))