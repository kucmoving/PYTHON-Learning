###0. new file like"my_file.txt
###https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

import pandas
data = pandas.read_csv("50_states.csv")

##1.0 抽取資料
##1.1選取特定column(假設是day, temp, condition)
print(data["temp"]
print(data.temp)

##1.2選取特定一row
print(data[data.day == "Monday"])

##1.3選取單獨一格
monday = data[data.day == "Monday"]
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(monday.condition)

##2.0進行計算(大量，要自己去看)
average = sum(temp_list) / len(temp_list)
print(average)
print(data["temp"].mean())
print(data["temp"].max())

##2.1計算該項有多少
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

##3.0 進行轉換
##3.1 將data轉成list
data = pandas.read_csv("weather_data.csv")
all_states = date.state.to_list()

##3.1 特定column轉換成dict
data_dict = data.to_dict()
temp_list = data["temp"].to_list()

