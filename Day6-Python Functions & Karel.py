#######################Day 6 Final Project: Escaping the Maze##################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    while not right_is_clear():
        turn_left()
    if right_is_clear():
        turn_right()
        move()
    elif not wall_in_front():
        move()
    else:
        turn_right()
        move()

################################################NOTES############################################
#Code Blocks#
indentation matters
the follwoing is a code block:
def my_function():
    print("Hello")


#Functions#
See https://docs.python.org/3/library/functions.html#func-list for built in functions
To create our own functions we use the prefix:
def my_function():
    print("Hello")
    print("Bye")
my_function()
The def prefix defines the function.
Calling the function just specifiy the name of the function.

#While Loops#
This keeps repeating a function WHILE a condition is true.
while something_is_true
    #do something repeatedly



##########################################CODE CHALLENGES#########################################\
#The Hurdles Loop Challenge: Reeborg's World#
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def hurdle():
    move()
    jump()
hurdle()
hurdle()
hurdle()
hurdle()
hurdle()
hurdle()
#OR#
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def hurdle():
    move()
    jump()
for step in range(6):
    hurdle()

#Hurdles Challenge using While Loops#
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles-= 1
#
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    jump()

#Hurdles dynamic path#
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#Final Hurdle! dynamic and variable height#
while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    elif front_is_clear():
        move()


