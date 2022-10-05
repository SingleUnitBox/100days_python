import datetime

import requests
import time
STOCK = "TWTR"
COMPANY_NAME = "Twitter"
API_KEY = "SMZHFW3F1LM2PQGK"
NEWS_API_KEY = "1c5a322ed48b46e39bae5f45f649dffb"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()
#print(data['Time Series (Daily)'])
list = [(key, value) for (key, value) in data['Time Series (Daily)'].items()]
price_today = float(list[0][1]['4. close'])
price_yesterday = float(list[1][1]['4. close'])
#print(price_today, price_yesterday)
price_diff = abs(float(price_yesterday) - float(price_today))
percent_change = price_diff/price_today * 100
if percent_change >= 1:
    print("get News")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
params_news = {
    "from": "2022-10-01",
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}
response_news = requests.get(url="https://newsapi.org/v2/everything", params= params_news)
response_news.raise_for_status()
data_news = response_news.json()
list_news = data_news['articles'][:2]
#print(list_news)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
if price_today > price_yesterday:
    print(f"+{round(percent_change, 2)}% '{COMPANY_NAME}' - {list_news[0]['title']}")
else:
    print(f"-{round(percent_change, 2)}%")

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

