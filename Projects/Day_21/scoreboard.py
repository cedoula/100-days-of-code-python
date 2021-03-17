from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Comic Sans MS", 24, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.score = 0
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER.", False, ALIGNMENT, FONT)