import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
screen.onkey(player.move, "Up")

game_is_on = True
game_loop_count = 0
moving_rate = STARTING_MOVE_DISTANCE
while game_is_on:
    time.sleep(0.1)
    
    game_loop_count +=1

    if game_loop_count % 6 == 0:
        car = CarManager()
    for car in screen.turtles():
        if car.shape() == "square":
            car.move()
            #Detect collision with car
            if player.distance(car) < 15:
                game_is_on = False
    if player.reached_finish_line():
        player.go_to_start_line()
        for car in screen.turtles():
            if car.shape() == "square":
                car.speed_up()
                print(car.moving_rate)


    screen.update()
    
    

screen.exitonclick()