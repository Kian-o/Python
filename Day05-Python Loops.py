#######################Day 5 Final Project: Password Generator################
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy mode - order not randomized#
let = random.sample(letters, k=nr_letters)
sym = random.sample(symbols, k=nr_symbols)
num = random.sample(numbers, k=nr_numbers)
test = let + sym + num
easypw = ""
for i in test:
  easypw += i
print(f"Here is the easy password: {easypw}")
#OR#
password = ""
for char in range(1, nr_letters +1):
  password += random.choice(letters)
for char in range(1, nr_symbols +1):
  password += random.choice(letters)
for char in range(1, nr_numbers +1):
  password += random.choice(numbers)
print(password)

#Hard mode - order randomized#
let = random.sample(letters, k=nr_letters)
sym = random.sample(symbols, k=nr_symbols)
num = random.sample(numbers, k=nr_numbers)
test2 = let + sym + num
random.shuffle(test2)
hardpw = ""
for i in test2:
  hardpw += i
print(f"Here is the hard password: {hardpw}")
#OR#
password = []
for char in range(1, nr_letters +1):
  password.append(random.choice(letters))
for char in range(1, nr_symbols +1):
  password.append(random.choice(symbols))
for char in range(1, nr_numbers +1):
  password.append(random.choice(symbols))
random.shuffle(password)
pw = ""
for char in password:
  pw += char
print(pw)




################################################NOTES###########################
#Loops!! For Loop
for item in list_of_items:
    Do something
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

#Range!
for number in range(1, 100):
    print(number)





##########################################CODE CHALLENGES########################
#Average Height#
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

students_total = 0
for student in student_heights:
  students_total += 1
print(f"student total = {students_total}")

average_height = round(total_height / students_total)
print(f"average height = {average_height}")


#High Scores#
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(highest_score)

#Adding Even Numbers#
total = 0
for number in range(1, 101):
  if number % 2 == 0:
    total += number
print(number)
#OR#
total = 0
for number in range(2, 101, 2):
  total += number
print(number)

#FixxBuzz Job Interview#
for number in range (1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)