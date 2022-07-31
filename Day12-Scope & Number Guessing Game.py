##### The Number Guessing Game ####
import art
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answers(guess, answer, turns):
    if guess > answer:
        print("Too High.")
        return turns - 1
    elif guess < answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(art.logo_number_guess)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = random.randrange(100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        turns = check_answers(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()

## First Draft

import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = random.randrange(100)
print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Choose easy or hard: ").lower()


def hard_mode():
    guess_attempts = 5
    game_over = False
    while game_over == False:
        print(f"You have {guess_attempts} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess == number:
            print(f"You got it! The answer was {number}")
            game_over = True
        elif user_guess > number:
            print("Too High")
            guess_attempts -= 1
        elif user_guess < number:
            print("Too Low")
            guess_attempts -= 1
        elif guess_attempts == 0:
            print("You've run out of guesses, you lose.")
            game_over = True

def easy_mode():
    guess_attempts = 10
    game_over = False
    while game_over == False:
        print(f"You have {guess_attempts} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess == number:
            print(f"You got it! The answer was {number}")
            game_over = True
        elif user_guess > number:
            print("Too High")
            guess_attempts -= 1
        elif user_guess < number:
            print("Too Low")
            guess_attempts -= 1
        elif guess_attempts == 0:
            print("You've run out of guesses, you lose.")
            game_over = True

if difficulty == "hard":
    hard_mode()
elif difficulty== "easy":
    easy_mode()






########### Scope #############
# In python, Scope mostly applies to functions. There is no blockscope in py.
#Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()
#Variable was created inside the function so it is only valid within the function

#Global Scope
player_health = 10
def drink_potion():
    potion_strength = 2
    print(player_health)
drink_potion()

#Modify Global Variables
enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#OR#
enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
#Namespace is anything that is given a name to. Namespaces are valid w/in specific scope

#Global Constants: naming convention is all caps seperated w underscores.
PI = 3.14159

def calc():
    PI



