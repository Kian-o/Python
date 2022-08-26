from turtle import Turtle, Screen
import turtle as t
import random

"""Million Dollar Painting!"""


"""Python Turtle"""
"""Timmy is a Red turtle Drawing a Square"""

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pendown()
for _ in range(4):
    timmy.forward(50)
    timmy.left(90)

print(timmy)

"""Tim is Drawing a Dashed Line"""

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

"""Tommy is Drawing Shapes"""


def draw_shape(num_sides):
    angle1 = 360 / num_sides
    tommy.pencolor(random.choice(colors))
    for _ in range(num_sides):
        tommy.forward(100)
        tommy.right(angle1)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

print(tommy)

screen = Screen()
screen.exitonclick()

"""Timothy is taking a Random Walk"""
timothy = Turtle()
timothy.shape("turtle")
colors = ["blue", "tomato", "indigo", "olive drab", "green", "light sky blue"]

list = [45, 90, -45, -90, 180, -180]


def walk(input_angle):
    timothy.pencolor(random.choice(colors))
    timothy.forward(100)
    timothy.right(input_angle)


def turtle_walk():
    return True


while turtle_walk():
    angle = int(random.choice(list))
    walk(angle)

screen = Screen()
screen.exitonclick()

"Timothy going on a Random Walk with LESS Code:"

timothy_is_shorter = t.Turtle()
timothy_is_shorter.shape("turtle")
colors = ["blue", "tomato", "indigo", "olive drab", "green", "light sky blue"]

list = [0, 90, 100, 270]

for _ in range(200):
    timothy_is_shorter.pencolor(random.choice(colors))
    timothy_is_shorter.pensize(15)
    timothy_is_shorter.forward(random.randint(10, 40))
    timothy_is_shorter.setheading(random.choice(list))

"""Aliasing Modules
import turtle as t
tim = t.Turtle()"""

"""Python Tuples: is a data type that looks like a list. Except Tuples are 
immutable. 
Ex: my_tuple = (1, 2, 3)
Ex: my_list = [1, 2, 3]"""

"""Terr the Random Colored frog"""

terry = t.Turtle()
t.colormode(255)
terry.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


list = [0, 90, 100, 270]

for _ in range(200):
    terry.pencolor(random_color())
    terry.pensize(15)
    terry.forward(random.randint(10, 40))
    terry.setheading(random.choice(list))

"""Spiro the Spirographic Turtle"""

spiro = t.Turtle()
t.colormode(255)
spiro.shape("turtle")
spiro.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


list = [0, 90, 100, 270]

for _ in range(360):
    spiro.pencolor(random_color())
    spiro.left(_)
    spiro.circle(50)

""""A prettier spirograph"""


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spiro.pencolor(random_color())
        spiro.setheading(spiro.heading() + size_of_gap)
        spiro.circle(100)


draw_spirograph(5)
"""Installing Modules
Modules that are not packaged with python library will need to be installed"""

screen = Screen()
screen.exitonclick()
