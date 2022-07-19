#######################Day 5 Final Project: Password Generator################





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