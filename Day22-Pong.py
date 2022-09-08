from turtle import Screen, Turtle
from pongpaddles import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle = Paddle()

screen.listen()
screen.onkey(fun=paddle.up, key="Up")
screen.onkey(fun=paddle.down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
