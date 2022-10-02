from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


# with open("data.txt") as file:
#     contents = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0, 260)
        self.write(f"Home: {self.score} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Home: {self.score} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh()
