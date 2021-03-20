from turtle import Turtle
from random import choice, uniform, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.moving_rate = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1,2,1)
            new_car.color(choice(COLORS))
            new_car.goto(310, uniform(-240,240))
            new_car.seth(180)
            new_car.speed("slowest")
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.moving_rate)

    def speed_up(self):
        self.moving_rate += MOVE_INCREMENT
        