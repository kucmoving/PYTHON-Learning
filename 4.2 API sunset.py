import requests
import datetime

time_now = datetime.datetime.now()

##加入formatted 會變成24小時制
parameters = {
    "lat": 22.396427,
    "lng": 114.109497,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
#要自己在打開JSON查看字典材可以知道有什麼可以抄寫
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
#split T 拿走T
#print(sunrise.split("T"))
##[1]是為了選取日期後的時間，split(":")是為了割開時、分、秒、毫秒
###print(sunrise.split("T")[1].split(":"))

##取去當中日出的的時間鐘數[0]
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

print(time_now.hour)

######設定條件如果現在是晚間
if time_now >= sunset or time_now <= sunrise:
    return True