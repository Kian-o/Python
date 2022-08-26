import turtle as t
import random

"""Python Turtle"""
spiro = t.Turtle()
t.colormode(255)
spiro.shape("turtle")
spiro.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


this_list_this_list = [0, 90, 100, 270]


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spiro.pencolor(random_color())
        spiro.setheading(spiro.heading() + size_of_gap)
        spiro.circle(100)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
