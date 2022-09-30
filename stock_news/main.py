import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


API_KEY_VANTAGE = "SMZHFW3F1LM2PQGK"
NEWS_API_KEY = "1c5a322ed48b46e39bae5f45f649dffb"

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

parameters = {

    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_VANTAGE,
}
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
close_price_yesterday = 123.55#float(data_list[0]['4. close'])
close_price_twodays_ago = 112.25#float(data_list[1]['4. close'])
diff = close_price_yesterday - close_price_twodays_ago


difference = abs(close_price_yesterday - close_price_twodays_ago)
diff_percent = (difference / close_price_yesterday) * 100
print(round(difference, 2))
print(round(diff_percent, 2))
if diff_percent > 5:
    print("Get News")


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
#https://newsapi.org/v2/everything?q=tesla&from=2022-08-30&sortBy=publishedAt&apiKey=1c5a322ed48b46e39bae5f45f649dffb
parameters_news = {

    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    #"language": "en"
}
response_news = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
response_news.raise_for_status()
data_news = response_news.json()
news_list = [value for (key, value) in data_news.items()]
new_list = news_list[2][:3]
article_list = [f"title: {article['title']}, author: {article['author']}" for article in new_list]


for article in article_list:
    if diff < 0:
        print(f"{(round(diff_percent, 2))}⬇ {article}")
    else:
        print(f"{(round(diff_percent, 2))}⬆ {article}")