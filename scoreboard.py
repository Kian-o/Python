from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("White")
        self.goto(0, 280)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
