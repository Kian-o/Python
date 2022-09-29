import time
from turtle import Screen
from turtle_crossing import Player, Scoreboard, CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing!")
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()




