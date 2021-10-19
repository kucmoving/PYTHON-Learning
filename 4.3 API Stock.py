#拿取API, 再進行REQUEST
import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "94X9IJZG7A3P2VC0"
NEWS_API_KEY = "fdb22b6891014f1fb3182f876b8c5c5a"

####連結套取JSON
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response =  requests.get(STOCK_ENDPOINT, params=stock_params)
print(response.json())

##收窄資料的位置
response =  requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
print(data)

##使用 comprehensionlist 令到佢變一格格，提取昨天價格
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#再前一天的價格
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#百份比變化
change = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) / float(day_before_yesterday_closing_price)
print(change)

#設定條件
if change > 0.03:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
