from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("White")
        self.goto(0, 260)
        self.write(f"Home: {self.l_score} Away: {self.r_score}", True, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Home: {self.l_score}  Away: {self.r_score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
