import time
from turtle import Screen
from food import Food
from snake import Snake
from snake_scoreboard import Scoreboard

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
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()


# Files
file = open("my_file.txt")
contents = file.read()
file.close()

with open("my_file.txt") as file:
    content = file.read()

with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# Mail Merge
with open("Mail Merge/invited_names.txt", "r") as f:
    name_list = f.readlines()

with open('Mail Merge/starting_letter.txt') as text_file:
    starting_letter = text_file.read()

for names in name_list:
    stripped_name = names.strip()
    new_letter = starting_letter.replace('[name]', stripped_name)
    with open(f'Mail Merge/ready_to_send/letter_for_{stripped_name}.txt', mode='w') as fp:
        fp.write(new_letter)