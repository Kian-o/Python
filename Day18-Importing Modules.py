from turtle import Turtle, Screen
import random

"""Python Turtle"""
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pendown()
for _ in range(4):
    timmy.forward(50)
    timmy.left(90)


print(timmy)

tim = Turtle()
tim.shape("turtle")
for _ in range(15):
    tim.pendown()
    tim.forward(15)
    tim.penup()
    tim.forward(15)


print(tim)


tommy = Turtle()
tommy.shape("turtle")
colors = ["blue", "tomato", "indigo", "olive drab", "green", "light sky blue"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    tommy.pencolor(random.choice(colors))
    for _ in range(num_sides):
        tommy.forward(100)
        tommy.right(angle)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

print(tommy)

screen = Screen()
screen.exitonclick()

"""Aliasing Modules"""
"""import turtle as t
tim = t.Turtle()"""


"""Installing Modules"""
"""Modules that are not packaged with python library will need to be installed"""







screen = Screen()
screen.exitonclick()


