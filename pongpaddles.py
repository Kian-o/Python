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


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()














