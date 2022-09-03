import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        scoreboard.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()


"""Classes can inherit methods from other classes"""
"""Below the Fish class inherits attributes from the Animal class"""
"""super() refers to the initial class (Animal)"""


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")

    def breathe(self):
        super().breathe()
        print("doing this in water")


nemo = Fish()
nemo.swim()
nemo.breathe()

"""Slicing Lists"""
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])
