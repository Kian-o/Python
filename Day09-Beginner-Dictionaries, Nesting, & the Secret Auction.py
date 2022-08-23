# from replit import clear
import art

"""SECRET AUCTION PROGRAM"""

print(art.logo_auction)
print("Welcome to the secret auction program")

over = False
bids = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} with a bid of ${highest_bid}")


while not over:
    name = input("What is your name? ").lower()
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    more = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if more == 'yes':
        clear()
    else:
        over = True
        find_highest_bidder(bids)

# for high in bidders


################################################NOTES###########################
"""Dictionaries
Every dictionary has a key and a value
{Key: Value}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}"""

"""Retrieving items from dictionary
print(programming_dictionary["Bug"])"""

"""Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."""

empty_dictionary = {"Add Something": "Something to add"}

"""Wipe an existing dictionary
programming_dictionary = {}"""

"""Edit item in Dictionary
programming_dictionary["Bug"] = "Changing the value in the key Bug"""

"""Loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])"""

"""Nesting Lists and Dictionaries##
Nesting- putting a dictionary or list inside of another dictionary.
{
    key: [List],
    Key2: {Dict}
}"""

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Berlin": ["Berlin", "Hamburg", "Stuttgart"],
}
dictionary_travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Berlin": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12},
}

"""Nesting a Dictionary inside of a list"""
list_dictionary_travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Berlin",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 12
    },
]

"""CODE CHALLENGES"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    if score > 80 and score <= 89:
        student_grades[student] = "Exceeds Expectations"
    if score > 70 and score <= 79:
        student_grades[student] = "Acceptable"
    if score <= 70:
        student_grades[student] = "Fail"
print(student_grades)

"""Dictionary in List"""

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
