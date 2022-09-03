from turtle import Screen, Turtle


screen = Screen()
screen.listen()
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_SIZE = 3


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for snake_index in STARTING_POSITIONS:
            self.add_segment(snake_index)

    def add_segment(self, position):
        james = Turtle("square")
        james.penup()
        james.color("white")
        james.goto(position)
        self.segments.append(james)

    def extend(self):
        self.add_segment(self.segments[-1].position())

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
