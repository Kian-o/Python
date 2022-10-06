import csv
import pandas
import numpy as np

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

