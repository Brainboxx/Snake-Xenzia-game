from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 8, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=230)
        self.pendown()
        self.score = 0
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def score_track(self):
        self.score += 1
        self.clear()
        self.update_score()
