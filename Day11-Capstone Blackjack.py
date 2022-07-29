import art
from random import randrange
import random

def blackjack():
    playing = input("Would you like to play blackjack? Type 'y' for yes or 'n' for no: ").lower()
    print(art.logo_blackjack)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    i = randrange(len(cards))
    cont = True
    def user_score():
        return sum(user_cards)

    def computer_score():
        return sum(computer_cards)

    if playing == "y":
        while cont:
            computer_cards = [cards[i], cards[i]]
            user_cards = [cards[i], cards[i]]
            user_score = user_score()

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
            elif computer_score > user_score and computer_score <= 21:
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


