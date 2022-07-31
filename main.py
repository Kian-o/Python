import art
import random
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose!"
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose. Computer has blackjack"
    elif user_score == 0:
        return "You win with blackjack!"
    elif user_score > 21:
        return "You went over!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def blackjack():
    print(art.logo)
    user_cards = []
    computer_cards = []
    cont = True

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while cont:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your score is {user_cards} {user_score}\n the computers first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            cont = False
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
                user_cards.append(deal_card())
            else:
                cont = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(
        f"Your final hand is: {user_cards}, and your Final score is: {user_score}\n The Computer's final hand is: {computer_cards}, and the Computer's final score is: {computer_score}\n {compare(user_score, computer_score)}")


while input("Would you like to play blackjack? Type 'y' for yes or 'n' for no: ").lower() == "y":
    clear()
    blackjack()