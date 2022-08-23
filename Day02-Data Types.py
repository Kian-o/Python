"""Day 2 Final Project: Tip Calculator"""

print("Welcome to the tip calculator! \n")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
party = int(input("How many people will split the bill? "))
individual = round(((bill*(tip/100) + bill)/party), 2)
print(f"Each person should pay: ${individual}")

"""OR"""

print("Welcome to the tip calulator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
individual = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
total_individual = "{:.2f}".format((bill_with_tip / individual))
print(f"Each person should pay: ${total_individual}")



"""NOTES"""

"Hello"[0]
"""counts the string characters"""

type()
"""is data type checking"""

str()
"""converts data type into string"""

float =()
"""converts data type into float"""

print(round(2.77777777, 2))
"""rounds the output to two decimal places - 2.78"""

print(8//3)
"""data type of result is int - 2"""

result = 4/2
result /= 2
print(result)
"""""""(+=) or (-=) or (/=) or (*=) is a way to manipulate a value based on previous value"""


score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")
"""f-Strings:  combines different data types in a single syntax"""

"""CODE CHALLENGES"""


"""Data Types"""
two_digit_number = input("Type a two digit number: ")
a = two_digit_number[0]
b = two_digit_number[1]
a1 = int(a)
b1 = int(b)
print(a1 + b1)

"""OR"""
two_digit_number = input("Type a two digit number: ")
a = two_digit_number[0]
b = two_digit_number[1]
result = int(a) + int(b)
print(result)


"""BMI Calculator"""
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
w = float(weight)
h = float(height)
bmi = w / (h**2)
result = int(bmi)
print(result)

"""OR"""
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)

"""Life in Weeks"""
age = input("What is your current age?")
time_left = 90-int(age)
months_left = time_left * 12
weeks_left = time_left * 52
days_left = time_left * 365
print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left.")
