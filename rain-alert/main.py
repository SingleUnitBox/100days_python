import requests
import os

parameters = {
    "lat": 52,
    "lon": 20,
    #"appid": "69f04e4613056b159c2761a9d9e664d2",
    "appid": os.environ.get("APPID"),
    "exclude": "current,minutely,daily",

}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
data_hourly = data["hourly"][:12]
for record in data_hourly:
    #if record["weather"][0]["id"] >= 700:
    print(record["weather"][0]["id"])




