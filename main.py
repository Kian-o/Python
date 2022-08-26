from turtle import Turtle, Screen
import random

"""Python Turtle"""
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
