from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("rectangle")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("black")
        self.goto(0, 260)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()
        self.color("green")

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_INCREMENT)
