import turtle as t
import random

color_list = [(212, 154, 97), (239, 246, 243), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97),
              (235, 240, 244), (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105), (54, 38, 20),
              (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126), (167, 21, 31), (225, 94, 78), (4, 30, 28),
              (39, 32, 34), (243, 163, 159), (81, 148, 168), (164, 27, 22), (239, 163, 167), (104, 123, 159),
              (164, 209, 193), (21, 81, 93), (29, 85, 81)]

turtle_hirst = t.Turtle()
turtle_hirst.shape("turtle")
turtle_hirst.penup()
turtle_hirst.speed("fastest")
turtle_hirst.pensize(20)
t.colormode(255)
turtle_hirst.setheading(255)
turtle_hirst.forward(300)
turtle_hirst.setheading(0)
number_of_dots = 100

for _ in range(1, number_of_dots + 1):
    turtle_hirst.dot(20, random.choice(color_list))
    turtle_hirst.forward(50)

    if _ % 10 == 0:
        turtle_hirst.setheading(90)
        turtle_hirst.forward(50)
        turtle_hirst.setheading(180)
        turtle_hirst.forward(500)
        turtle_hirst.setheading(0)


screen = t.Screen()
screen.exitonclick()
