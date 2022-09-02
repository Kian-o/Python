from turtle import Screen, Turtle
import random

screen = Screen()
screen.listen()
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for snake_index in range(0, 3):
            james = Turtle("square")
            james.penup()
            james.color("white")
            james.goto(x=(snake_index * -20), y=0)
            self.segments.append(james)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            # self.head.forward(MOVE_DISTANCE)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            # self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            # self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            # self.head.forward(MOVE_DISTANCE)

# class Food:
#
#     def __init__(self):
#
#
#     def drop(self):
#         spot = Turtle()
#         spot.hideturtle()
#         while
