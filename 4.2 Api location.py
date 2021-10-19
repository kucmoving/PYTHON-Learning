##插入requests
import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")

#檢查連線狀態
print(response.status_code)
#睇下有冇error
print(response.raise_for_status())
data = response.json()

#讀出當中的數據(因應字典再讀)
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])
iss_position = (longitude, latitude)
print(iss_position)

###設定條件(如果太空站與自己的距離...
if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
    return True


#自己的座標
#https://www.latlong.net/Show-Latitude-Longitude.html


##########較難的API參數加入###############

MY_LAT = 22.396427
MY_LONG = 114.109497

parameters = {
    MY_LAT: 22.396427,
    MY_LONG: 114.109497,
}
response2 = requests.get("https://api.sunrise-sunset.org/json", params = parameters)

response2.raise_for_status()
data = response2.json()
print(data)

## Endpoint / ? / param name = value & param name = value & param name = value &…..



