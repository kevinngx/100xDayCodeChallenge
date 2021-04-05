# with open("weather_data.csv") as data:
#     data_list = data.readlines()

# for item in data_list:
#     print item

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if (row[1] != "temp"):
#             temperatures.append(int(row[1]))

# for temperature in temperatures:
#     print(str(temperature))

import pandas as pd

data = pd.read_csv("weather_data.csv")

# Print attributes
# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in a columns
# print(data.condition)

# Print a specific row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp * 1.8 + 32)

# Create a dataframe from scratch
data_dict = { 
    "students": ["Amy", "James", "Angel"],
    "scores": [76, 82, 91]
}

new_data = pd.DataFrame(data_dict)
new_data.to_csv("new_data.csv")


