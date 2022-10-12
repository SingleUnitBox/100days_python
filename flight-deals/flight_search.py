import requests
from flight_data import FlightData

tequila_apikey = "elSC1X-HeRAR_xoycl-iJU4mNKVZoky8"
tequila_endpoint = "https://api.tequila.kiwi.com"



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        header = {
            "apikey": tequila_apikey,
        }
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{tequila_endpoint}/locations/query", headers=header, params=query)
        code = response.json()['locations'][0]['code']
        return code

    def search_cheap_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {
            "apikey": tequila_apikey,
        }
        search = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "flight_type": "round",
            "max_stopovers": 0,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "one_for_city": 1

        }
        response = requests.get(
            url=f"{tequila_endpoint}/v2/search",
            headers=header,
            params=search
        )
        try:
            data = response.json()['data'][0]
        except IndexError:
            print("No flights found for {}")
            return None

        flight_data = FlightData(
            price = data["price"],
            origin_city = data["cityFrom"],
            origin_airport = data["flyFrom"],
            destination_city = data["cityTo"],
            destination_airport = data['flyTo'],
            out_date = data["route"][0]['local_departure'].split("T")[0],
            return_date = data["route"][1]['local_departure'].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
