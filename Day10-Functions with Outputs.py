import art

"""Calculator App"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo_calc)
    number1 = float(input("What's the first number? "))
    for thing in operations:
        print(thing)
    proceed = True

    while proceed:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = round(calculation_function(number1, num2), 2)
        print(f"{number1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower() == "y":
            number1 = answer
        else:
            proceed = False
            calculator()


calculator()

"""OR"""

print(art.logo_calc)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number? "))
for key in operations:
    print(key)

operation_symbol = input("Pick an operation: ")
num2 = int(input("What's the next number? "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
cont = True
while cont:
    another = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
    if another == 'n':
        count = False
    else:
        operation_symbol = input("Pick an operation: ")
        num3 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(answer, num3)

print(f"{num1} {operation_symbol} {num3} = {answer}")

"""NOTES"""
"""Functions with inputs allow you to change the code in the function to do something different each time
Functions with outputs allow you to have an output once the function is completed"""


def my_function():
    result = 3 * 2
    return result


output = my_function

"""Multiple Returns"""


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))

"""Why not Print?"""

"""CODE CHALLENGES"""

"""Whats your name?"""


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


f_name = input("First Name? ")
l_name = input("Last Name? ")

print(format_name(f_name, l_name))

"""Days in Month"""


def is_leap(this_year):
    if this_year % 4 == 0:
        if this_year % 100 == 0:
            if this_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(another_year, another_month):
    if another_month > 12 or another_month < 1:
        return "Invalid Match"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(another_year):
        return month_days[another_month - 1] - 1
    else:
        return month_days[another_month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
