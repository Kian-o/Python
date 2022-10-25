# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)
#
# name = 'Michael'
# name_list = [letter for letter in name]
#
# print(name_list)
#
# double_list = [number * 2 for number in range(1, 5)]
# print(double_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
big_names = [name.upper() for name in names if len(name) > 5]
