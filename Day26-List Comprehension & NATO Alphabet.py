# List and Dictionary Comprehensions

new_list = [new_item for item in list]

# See example below for For Loop then List comprehension
# For Loop:
numbers = [1, 2, 3]
new_list = []
for n in list:
    add_1 = n + 1
new_list.append(add_1)

# List Comprehension

new_list = [n+1 for n in numbers]

name = 'Michael'
name_list = [letter for letter in name]

double_list = [number * 2 for number in range(1, 5)]
print(double_list)

# Conditional List Comprehension
new_list = [new_item for item in list if test]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
big_names = [name.upper() for name in names if len(name) > 5]
