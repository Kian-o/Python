from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0)
#
# segments = []
#
# for snake_index in range(0, 3):
#     james = Turtle("square")
#     james.penup()
#     james.color("white")
#     james.goto(x=(snake_index * -20), y=0)
#     segments.append(james)
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#
#     for seg_num in range(len(segments) - 1, 0, -1):
#         segments[seg_num].goto(segments[seg_num - 1].xcor(), segments[seg_num - 1].ycor())
#
#     segments[0].forward(20)
#     segments[0].left(90)

screen.exitonclick()


class snake:
    segments = []
    screen.listen()
    screen.onkey(key="w", fun=forwards)
    screen.onkey(key="s", fun=backwards)
    screen.onkey(key="a", fun=left)
    screen.onkey(key="d", fun=right)
    screen.onkey(key="c", fun=erase)

    for snake_index in range(0, 3):
        james = Turtle("square")
        james.penup()
        james.color("white")
        james.goto(x=(snake_index * -20), y=0)
        segments.append(james)

    for seg_num in range(len(segments) - 1, 0, -1):
        segments[seg_num].goto(segments[seg_num - 1].xcor(), segments[seg_num - 1].ycor())

    def forwards():
        segments[0].forward(20)

    def backwards():
        segments[0].backward(20)

    def left():
        segments[0].left(45)

    def right():
        segments[0].right(45)
