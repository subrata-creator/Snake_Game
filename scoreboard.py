from turtle import Turtle

ALLIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score :{self.score}", align=ALLIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALLIGN, font=FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_score()
