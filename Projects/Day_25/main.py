from pathlib import Path

path = Path(__file__).parent / "./weather_data.csv"
# with open(path, "r") as file:
#     list = file.readlines()
# print(list)

import pandas as pd

# import csv
# with open(path) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pd.read_csv(path)
print(dat["temp")