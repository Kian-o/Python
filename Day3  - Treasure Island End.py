#Day 3 Final Project: Treasure Island############################################
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")
if direction1.lower() == "right":
    print("You fell into a hole. Game Over.")
else:
    direction2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
if direction2.lower() == "swim":
    print("Attacked by trout. Game Over.")
else:
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
if door.lower() == "red":
    print("Burned by fire. Game Over.")
elif door.lower() == "yellow":
    print("You Win!")
elif door.lower() == "blue":
    print("Eaten by beasts. Game Over.")
else:
    print("Game Over.")









################################################NOTES##############################################

# Control FLow with if/else Conditional Operators#
# if condition:
#     do_this
# else:
#     do_this
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Modulo: (%) returns the remainder of a division

#Nested if statements and elif statements#
# if condition:
#     if another condition:
#        do_this
# else:
#     do_this
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age >= 12 and age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

#Multiple If statements in succession#
# if condition1:
#   do A
#if condition2:
#   do B
# if condition3:
#   do C
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adults tickets are $12.")
    wants_photo = input("Would you like a photo? Y or N ")
    if wants_photo == "Y":
        bill += 3
    print(f"Please pay ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
# adding to a variable you can use (+=) for subtracting you can use (-=)

#Logical Operators#
# How to combine conditions? AND, OR, & NOT
# a = 12
# a > 10 and a < 13

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age >= 12 and age < 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Midlife crisis tickets are $0.")
    else:
        bill = 12
        print("Adults tickets are $12.")
    wants_photo = input("Would you like a photo? Y or N ")
    if wants_photo == "Y":
        bill += 3
    print(f"Please pay ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")


##########################################CODE CHALLENGES###########################################


#Odd or Even?#
number = int(input("Which number do you want to check? "))
modulo = number % 2
if modulo >= 1:
    print("This is an odd number.")
else:
    print("This number is even.")
#OR#
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#BMI 2.0#
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
w = float(weight)
h = float(height)
bmi = round(w / (h**2))
if bmi <= 18.5:
  print(f"Your BMI is {bmi}. You are underweight.")
elif bmi > 18.5 and bmi <=25:
  print(f"Your BMI is {bmi}. You are normal weight.")
elif bmi > 25 and bmi <= 30:
  print(f"Your BMI is {bmi}. You are overweight.")
elif bmi > 30 and bmi <= 35:
  print(f"Your BMI is {bmi}. You are obese.")
elif bmi > 35:
  print(f"Your BMI is {bmi}. You are clinically obese.")
#OR#
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
w = float(weight)
h = float(height)
bmi = round(w / (h**2))
if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}. You are obese.")
else:
    print(f"Your BMI is {bmi}. You are clinically obese.")

#Leap Year#
year = int(input("Which year do you want to check? "))
if year % 4 >= 1:
    print("This is not a leap year.")
elif year % 100 >= 1:
    print("This is not a leap year")
elif year % 400 >= 1:
    print("This is not a leap year.")
else:
    print("This is a leap year.")
#OR#
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
        else:
            print("Leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

#Pizza Order Practice#
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill += 25
    if add_pepperoni =="Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")
#OR#
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni =="Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")

#Love Calculator#
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
names = (name1 + name2).lower()
T = names.count("t")
R = names.count("r")
U = names.count("u")
E = names.count("e")
true_count = T + R + U + E
L = names.count("l")
O = names.count("o")
V = names.count("v")
love_count = L + O + V + E
score = str(true_count) + str(love_count)
score = int(score)
if score <= 10 and score >= 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}")

