###########Calculator App#########################






################################################NOTES###########################
Functions with inputs allow you to change the code in the function to do something different each time
Functions with outputs allow you to have an output once the function is completed
def my_function():
    result = 3 * 2
    return result
return 3 * 2
output = My_function

"""Multiple Returns"""
def format_name(f_name, l_name):
   if f_name == "" or l_name == "":
     return "You didn't provide valid inputs."
   formated_f_name = f_name.title()
   formated_l_name = l_name.title()
   return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

"""Why not Print?"""






##########################################CODE CHALLENGES#####################
#Whats your name?
def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

f_name = input("First Name? ")
l_name = input("Last Name? ")

print(format_name(f_name, l_name))

#Days in Month#
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid Match"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        return month_days[month - 1] - 1
    else:
        return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
