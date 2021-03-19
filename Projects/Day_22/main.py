from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from line import Line

RIGHT = (350,0)
LEFT =(-350,0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(RIGHT)
l_paddle = Paddle(LEFT)
ball = Ball()
scoreboard = ScoreBoard()
line = Line()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "e")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()

    #Detect collision with top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_on_wall()

    #Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_on_r_paddle()
        ball.increase_ball_speed()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_on_l_paddle()
        ball.increase_ball_speed()

    #Detect out of bounds
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()

    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()

screen.exitonclick()