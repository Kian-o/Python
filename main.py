import csv

import pandas

data = pandas.read_csv('squirrel_count.csv')

fur_color_list = data['Primary Fur Color'] = data['Primary Fur Color'].to_list()

color_dict = {
    'Fur Color': ['gray', 'cinnamon', 'black'],
    'Count': [fur_color_list.count('Gray'), fur_color_list.count('Cinnamon'), fur_color_list.count('Black')]
}
color_count = pandas.DataFrame(color_dict)

print(color_count)

# data_dict = data.to_dict()




# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #
# # print(temperatures)
# import pandas
# import numpy as np
#
# data = pandas.read_csv('weather_data.csv')
# data_dict = data.to_dict()
# print(data_dict)
#
# # temp_list = data['temp'] = data['temp'].to_list()
# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)
# #
# # print(data['temp'].mean())
# #
# # print(np.mean(temp_list))
# #
# # print(data['temp'].max())
#
# # print(data[data.temp == data.temp.max()])
# #
# monday = data[data.day == 'Monday']
# print((monday.temp * 1.8) + 32)
#
# data_dict = {
#     "students": ['Amy', 'James', 'Angela'],
#     "scores": [76, 56, 65]
# }
# datas = pandas.DataFrame(data_dict)
# datas.to_csv('new_data.csv')
# print(datas)
