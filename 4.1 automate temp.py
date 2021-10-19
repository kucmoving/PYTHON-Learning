import smtplib
import datetime ##第一個是module, 第二個是class

####設定好時間機制
now = datetime.datetime.now()
weekday = now.weekday()
time_tuple = (now.year, now.month, now.day)

####打開文件
import pandas
data = pandas.read_csv('birthdays.csv') #用pandas 打開csv
birthdays_dict = {(date_row["month"], date_row["day"]): date_row for (index, date_row) in data.iterrows()}
#使用COMPRE LOOP 設定格式

####設定觸發機制，如果是星期1...就打開文件 / 如果日期在表格中有，就隨機選取文字，取代名字送出
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
    print(quote)

import random
if time_tuple in birthdays_dict:
    birthday_person = birthdays_dict[time_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.text"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace["[NAME]", birthday_person["name"]]


##設定條件成立時不停生效
while:
    time.sleep(60) #60秒執行一次
    if is_iss_overhead() and is night():
        ####加入email動作
