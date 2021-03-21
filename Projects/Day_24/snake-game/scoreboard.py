from turtle import Turtle
import os
ALIGNMENT = "center"
FONT = ("Comic Sans MS", 24, "bold")
file_to_load = os.path.join("/Users/Cedoula/Desktop/100DaysOfCode/100-days-of-code/Projects/Day_24/snake-game", "data.txt")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.score = 0
        with open(file_to_load, "r") as file:
            self.high_score = int(file.read())
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  -  High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.refresh_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file_to_load, "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.refresh_scoreboard()


    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER.", False, ALIGNMENT, FONT)