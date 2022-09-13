from turtle import Turtle

MOVE_DISTANCE = 30
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.ht()
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.st()

    def down(self):
        self.goto(self.xcor(), (self.ycor() - MOVE_DISTANCE))

    def up(self):
        self.goto(self.xcor(), (self.ycor() + MOVE_DISTANCE))


class Ball():

    def __init__(self):
        super().__init__()
        self.shape("circle")













    # def create_paddle(self, position):
    #     paddle = Turtle("square")
    #     self.ht()
    #     self.penup()
    #     self.color("white")
    #     self.shapesize(stretch_wid=5, stretch_len=1)
    #     self.goto(position)
    #     self.st()
    #     self.segments.append(paddle)