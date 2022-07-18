#######################Day 4 Final Project: Rock Paper Scissors############################################
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


options = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(options[choice])

computer_choice = random.randint(0,2)
print(f"Computer chooses:\n {options[computer_choice]}")

if choice == 0 and computer_choice == 2:
  print("You Win")
elif choice == 1 and computer_choice == 0:
  print("You Win")
elif choice == 2 and computer_choice == 1:
  print("You Win")
elif choice == computer_choice:
  print("Its a draw!")
else:
  print("You Lose")









################################################NOTES##############################################
#Machines are Deterministic. Maths can be applied to create psuedorandom number genreators. Mersenne Twister is what Python uses.
https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
import random
random_integer = random.randint(1, 10)
print(random_integer)
random_float = random.random() * 5
print(random_float)
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Modules help break up large complex code blocks. Modules are the .py files inside the larger project file.
import different_module
import day4_import
print (day4_import.pi)

# LISTS # 43
# the list is a data structure: way of organizing/storing data in .py
# Store grouped pieces of data
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america)

# could also store objects in a variable:
fruits =(item1, item2)

# order is also set when the list is created. The following code will print the first item in the list.
# Using negative index print(states_of_america[-1]) it will pull from the rear of the list.
#Also this list was created in the order the states joined the union. ex:
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[0])

# Use square brackets to create list and pull data out of list
# []
# Can modify the list using square brackets also:
states_of_america[1] = "Pencilvania"

# or add items:
states_of_america.append("New_State")

# You can pull random items in a list by using
random.choice(seq)

# or remove items, there are many functions that can be used on lists. See:
https://docs.python.org/3/tutorial/datastructures.html

# IndexErrors
# Indexes start counting at 0. The first list item is ordered as #0 then 1,2,3,4.
# If the list has 50 items and you need to pull the 50th you would write:
print(states_of_america[49])
# or
import random
random_integer = random.randint(0, (len(states_of_america)-1))

# Nested Lists#
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen =[fruits, vegetables]

##########################################CODE CHALLENGES###########################################
# Heads or Tails #
import random
result = random.randint(0,1)
if result == 0:
  print("Heads")
else:
  print("Tails")

# Banker Roulette - Who will pay the bill? #
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random
random_integer = random.randint(0, (len(names)-1))
payer = names[random_integer]
print(f"{payer} is going to buy the meal today!")

# Treasure Map#
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
a = int(position[0])
b = int(position[1])
if a == 1 and b == 1:
  row1[0] = "X"
elif a == 2 and b == 1:
  (row1[1]) = "X"
elif a == 3 and b == 1:
  row1[2] = "X"
elif a == 1 and b == 2:
  row2[0] = "X"
elif a == 2 and b == 2:
  row2[1] = "X"
elif a == 3 and b == 2:
  row2[2] = "X"
elif a == 1 and b == 3:
  row3[0] = "X"
elif a == 2 and b == 3:
  row3[1] = "X"
else:
  row3[2] = "X"
print(f"{row1}\n{row2}\n{row3}")
#OR#
a = int(position[0])
b = int(position[1])
row = map[b-1]
row[a-1] = "X"
#OR#
a = int(position[0])
b = int(position[1])
row = map[b-1][a-1] = "X"




