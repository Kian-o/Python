from turtle import Screen, Turtle
from pongpaddles import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(fun=Paddle.up, key="Up")
screen.onkey(fun=Paddle.down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
