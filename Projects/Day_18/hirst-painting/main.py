import colorgram
import turtle as t
from turtle import Turtle, Screen
from random import choice

# Extract 40 colors from the image.
# colors = colorgram.extract("/Users/Cedoula/Desktop/100DaysOfCode/100-days-of-code/Projects/Day_18/hirst-painting/image.jpeg", 40)
# colors_rgb = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
# print(colors_rgb)

color_list = [(198, 12, 32), (250, 237, 17), (39, 77, 189), (38, 217, 67), (238, 228, 5), (229, 159, 46), (27, 39, 158), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 247, 252), (244, 33, 165), (229, 17, 122), (73, 9, 31), (60, 14, 8), (224, 141, 211), (222, 160, 8), (10, 98, 61), (17, 18, 43), (47, 214, 232), (11, 227, 239), (79, 72, 215), (237, 155, 222), (73, 213, 169), (78, 234, 201), (50, 234, 244), (3, 66, 40), (222, 86, 44), (174, 178, 231), (5, 246, 222), (251, 7, 48), (235, 169, 164), (10, 80, 111), (14, 51, 246), (244, 14, 14)]

tim = Turtle()
tim.penup()
t.colormode(255)
tim.speed('fastest')
tim.hideturtle()

for i in range(10):
    tim.setpos(-225,-200 + 50 * i)
    for _ in range(10):
        tim.pendown()
        tim.dot(20, choice(color_list))
        tim.penup()
        tim.forward(50) 

screen = Screen()
screen.exitonclick()