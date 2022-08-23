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
    print(art.logo_blackjack)
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

"""ROUGH DRAFT"""


def blackjack():
    playing = input("Would you like to play blackjack? Type 'y' for yes or 'n' for no: ").lower()
    print(art.logo_blackjack)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    i = random.randrange(len(cards))
    cont = True

    def deal_card():
        user_cards.append(cards[i])
        computer_cards.append(cards[i])

    if playing == "y":
        while cont:
            computer_cards = [cards[i], cards[i]]
            computer_score = sum(computer_cards)
            user_cards = [cards[i], cards[i]]
            user_score = sum(user_score)

            print(f"your score is {user_cards} {user_score}\n the computers first card is {computer_cards}")
            if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
                user_cards.append(cards[i])
                user_score = sum(user_cards)
                computer_score = sum(computer_cards)
                computer_cards.append(cards[i])
                if user_score >= 22:
                    print(
                        f"Your final hand: {user_cards}, final score: {user_score}\n Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You went over. You lose.")
                    cont = False
                    blackjack()
                elif computer_score >= 22:
                    print(
                        f"Your final hand: {user_cards}, final score: {user_score}\n Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("The computer went over! YOU WIN!")
                    cont = False
                    blackjack()
                elif computer_score == user_score:
                    print(
                        f"Your final hand: {user_cards}, final score: {user_score}\n Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("It was a draw!")
                    cont = False
                    blackjack()
                else:
                    cont = False
                    print(
                        f"Your final hand: {user_cards}, final score: {user_score}\n Computer's final hand: {computer_cards}, final score: {computer_score}")
            elif user_score < computer_score <= 21:
                print("You Lose!")
            elif computer_score == user_score:
                print("It was a draw!")
            else:
                print("You Win!")
                blackjack()


blackjack()

# while cont:
#     computer_cards = [cards[i], cards[i]]
#     user_cards = [cards[i], cards[i]]
#
#     print(f"your score is {user_cards} {user_score}\n the computers first card is {computer_cards}")
#     if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
#             user_cards.append(cards[i])
#             user_score = sum(user_cards)
#             computer_score = sum(computer_cards)
#             computer_cards.append(cards[i])
#             if user_score >= 22:
#                 print(f"Your final hand: {user_cards}, final score: {user_score}\n Computer's final hand: {computer_cards}, final score: {computer_score}")
#                 print("You went over. You lose.")
#                 cont = False
#                 blackjack()
#             elif computer_score >= 22:
#                 print(f"Your final hand: {user_cards}, final score: {user_score}\n Computer's final hand: {computer_cards}, final score: {computer_score}")
#                 print("The computer went over! YOU WIN!")
#                 cont = False
#                 blackjack()
#             elif computer_score == user_score:
#                 print(f"Your final hand: {user_cards}, final score: {user_score}\n Computer's final hand: {computer_cards}, final score: {computer_score}")
#                 print("It was a draw!")
#                 cont = False
#                 blackjack()
#             else:
#                 cont = False
#                 print(f"Your final hand: {user_cards}, final score: {user_score}\n Computer's final hand: {computer_cards}, final score: {computer_score}")
#     elif computer_score > user_score and computer_score <= 21:
#         print("You Lose!")
#     elif computer_score == user_score:
#          print("It was a draw!")
#     else:
#          print("You Win!")
#          blackjack()
