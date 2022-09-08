from turtle import Turtle

MOVE_DISTANCE = 10
UP = 90
DOWN = 270


class Paddle:

    def __init__(self):
        self.segments = []
        self.create_paddle()
        self.head = self.segments[0]

    # def create_paddle(self):
    #     for paddle_index in STARTING_POSITIONS:
    #         self.add_segment(paddle_index)

    def create_paddle(self):
        paddle = Turtle("square")
        paddle.penup()
        paddle.color("white")
        paddle.shapesize(stretch_wid=4, stretch_len=1)
        paddle.goto(360, 0)
        self.segments.append(paddle)

    def down(self):
        self.head.setheading(DOWN)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(UP)
        self.head.forward(MOVE_DISTANCE)
