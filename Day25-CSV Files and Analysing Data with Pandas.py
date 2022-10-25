import csv
import pandas
import numpy as np
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('us-states-game-start/50_states.csv')
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's "
                                                                                            "name?").title()
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

turtle.mainloop()

turtle.shape(image)

data = pandas.read_csv('squirrel_count.csv')

fur_color_list = data['Primary Fur Color'] = data['Primary Fur Color'].to_list()

color_dict = {
    'Fur Color': ['gray', 'cinnamon', 'black'],
    'Count': [fur_color_list.count('Gray'), fur_color_list.count('Cinnamon'), fur_color_list.count('Black')]
}
color_count = pandas.DataFrame(color_dict)
color_count.to_csv('squirrel_fur_count.csv')
print(color_count)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

print(temperatures)

# Or

data = pandas.read_csv('weather_data.csv')
print(data['temp'])

# Or

data = pandas.read_csv('weather_data.csv')
data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'] = data['temp'].to_list()
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

print(data['temp'].mean())

print(np.mean(temp_list))

print(data['temp'].max())

# Query on the row

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)


# Mondays temp in Fahrenheit
monday = data[data.day == 'Monday']
print((monday.temp * 1.8) + 32)

# Create a data-frame from scratch
data_dict = {
    "students": ['Amy', 'James', 'Angela'],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

# Squirrel Data

data = pandas.read_csv('squirrel_count.csv')

fur_color_list = data['Primary Fur Color'] = data['Primary Fur Color'].to_list()

color_dict = {
    'Fur Color': ['gray', 'cinnamon', 'black'],
    'Count': [fur_color_list.count('Gray'), fur_color_list.count('Cinnamon'), fur_color_list.count('Black')]
}
color_count = pandas.DataFrame(color_dict)

print(color_count)
