##https://docs.python.org/3/library/datetime.html 處理時間

##進行匯入，Module>class
#1) 展示現在的時間
import datetime
now = datetime.datetime.now()
print(now)
#會出現 2020-07-14 09:24:52.199356

#2)在此之後展示now的數據
year = now.year         #本年
month = now.month       #今月
day = now.day           #今天
hour = now.hour
weekday = now.weekday() #本星期
time_tuple = (now.year, now.month, now.day)

#會出現1

#3)輸入日期的位置
date_of_birth = datetime.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)
#會出現 1995-12-15 04:00:00

#4)今天的時間
now = datetime.datetime.now()
month = now.month
day = now.day
today = (month, day)

#今天時間
print(now.strftime("%Y%m%d"))