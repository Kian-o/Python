# 1. Describe the Problem
# 2. Reproduce the bug
# 3. Play Computer
# 4. Fix the Errors
# 5. Print is your friend
# 6. Use a Debugger: Thonny or https://pythontutor.com/render.html#mode=display
# 7. Take a break
# 8. Ask a friend
# 9. Run often
# 10. Ask StackOverflow


##### Debugging Odd or Even #####
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#FIX#
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


##### Debugging Leap Year #####
year = input("Which year do you want to check?")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

#FIX#
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


##### Debugging FizzBuzz #####
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])

#FIX#
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])