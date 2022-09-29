from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
FINISH_LINE_Y = 280
MOVE_INCREMENT = 10
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class CarManager:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        # self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.penup()
        self.pencolor("black")
        self.goto(-260, 260)
        self.write(f"Level: {self.score}", True, align='left', font=('Arial', 12, 'normal'))

    def refresh(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Level: {self.score}", True, align='left', font=('Arial', 12, 'normal'))

    def next_level(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!\n Final Level: {self.score}", align='center', font=('Arial', 24, 'normal'))


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.showturtle()
        self.color("green")

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

