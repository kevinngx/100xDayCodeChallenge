import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data.groupby("Primary Fur Color").count())

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "color": ["Gray", "Cinnamon", "Black"],
    "count": [grey_count, cinnamon_count, black_count]
}

pd.DataFrame(data_dict).to_csv("squirrel_count.csv")
