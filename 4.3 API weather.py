##https://home.openweathermap.org/api_keys
##https://openweathermap.org/current
##https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=a3cf6984482c835d5bc6bbd134f7161c
###https://openweathermap.org/api/one-call-api

##http://jsonviewer.stack.hu/#http://

import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a3cf6984482c835d5bc6bbd134f7161c"

weather_params = {
    "lat": 22.396427,
    "lon": 114.109497,
    "appid": api_key,
    "exclude": "current, minutely, daily" ###這部份要看docu, 及json，才知道哪些可以被刪) / 否則會抽取全部
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
##print(weather_data["hourly"][0]["weather"][0]["id"]) #一層層打開json
##因為數據在api中是分佈在不同位置，要用slice將dict割開
weather_slice = weather_data["hourly"][:12]

##用forloop 抽取相關資料,再設定條件
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"] #這syntax會在slice下再挖入去
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("bring an umbrella.")