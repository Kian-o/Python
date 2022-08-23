from day14_game_data import data
from art import vs, logo_higherlower
import random


# from replit import clear


def get_random_selection():
    return random.choice(data)


def data_format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, {country}."


def check_answers(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo_higherlower)
    score = 0
    game_continue = True
    account_a = get_random_selection()
    account_b = get_random_selection()

    while game_continue:
        account_a = account_b
        account_b = get_random_selection()

        while account_a == account_b:
            account_b = get_random_selection

        print(f"Compare a: {data_format(account_a)}")
        print(vs)
        print(f"Against B: {data_format(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answers(guess, a_follower_count, b_follower_count)

        # clear()
        print(logo_higherlower)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_continue = False
            print(f"Sorry, that is incorrect! Final score is {score}")


game()
