"""Notes"""
"""OOP: Object Oriented Programming
Procedural programming: One of the earliest paradigms of programming.
Confusing and outdated and hard to manage
OOP: Breaks problems down into several modules. Modules become reusable.
Object: What it Has (Attributes) and What it Does (Methods).
Classes: Hierarchy of multiple objects. Several different objects can live in one Class
Constructing Objects: The class provides the blueprint for the object.
car = CarBlueprint() the car is the object and the CarBlueprint() is the class"""

"""Turtle Graphics"""

from turtle import Turtle

timmy = Turtle()
print(timmy)

"""Object Attributes: car.speed -car is the object and the . is the attribute"""

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)

"""Object Methods: (functions): car.stop() -car is the object and .stop() is the function or method"""

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

"""Attributes and Methods"""

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("violet")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
