import requests

tequila_apikey = "elSC1X-HeRAR_xoycl-iJU4mNKVZoky8"
tequila_endpoint = "https://api.tequila.kiwi.com"

def search_cheap_flight():
    header = {
        "apikey": tequila_apikey,
    }
    search = {
        "fly_from": "LON",
        "fly_to": "PAR",
        "flight_type": "round",
        "max_stopovers": 0,
        "date_from": "13/10/2022",
        "date_to": "13/04/2023",
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "curr": "GBP",
        "one_for_city": 1

    }
    response = requests.get(url=f"{tequila_endpoint}/v2/search", headers=header, params=search)
    data = response.json()
    print(data)

search_cheap_flight()