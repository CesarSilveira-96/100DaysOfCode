
# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()

#
# import csv
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# Squirrel Analysis

sq_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_sq_count = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
red_sq_count = len(sq_data[sq_data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(sq_data[sq_data["Primary Fur Color"] == "Black"])

print(gray_sq_count)
print(red_sq_count)
print(black_sq_count)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray_sq_count,red_sq_count,black_sq_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("Squirrel_Colors_Count.CSV")
