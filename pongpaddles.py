from turtle import Turtle

MOVE_DISTANCE = 30
UP = 90
DOWN = 270


class Paddle:

    def __init__(self, position):
        self.segments = []
        self.position = position
        self.create_paddle(self.position)
        self.head = self.segments[0]

    def create_paddle(self, position):
        paddle = Turtle("square")
        paddle.ht()
        paddle.penup()
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.goto(position)
        paddle.st()
        self.segments.append(paddle)

    def down(self):
        self.head.goto(self.head.xcor(), (self.head.ycor() - MOVE_DISTANCE))

    def up(self):
        self.head.goto(self.head.xcor(), (self.head.ycor() + MOVE_DISTANCE))
