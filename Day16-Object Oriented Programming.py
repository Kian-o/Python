from turtle import Turtle, Screen
from prettytable import PrettyTable
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

coffee_on = True

while coffee_on:
    choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if choice == 'off':
        coffee_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink):
            CoffeeMaker.make_coffee(drink)


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

timmy = Turtle()
print(timmy)

"""Object Attributes: car.speed -car is the object and the . is the attribute"""

timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)

"""Object Methods: (functions): car.stop() -car is the object and .stop() is the function or method"""

timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

"""Attributes and Methods"""

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("violet")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


"""PrettyTable"""

table = PrettyTable()
print(table)

x = PrettyTable()
x.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
x.add_column("Type", ["Electric", "Water", "Fire"])
x.align = "l"
print(x)

