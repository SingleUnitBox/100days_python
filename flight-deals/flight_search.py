from pprint import pprint

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
            print(f"No flights found for {destination_city_code}")
            search["max_stopovers"] = 2
            response = requests.get(
                url=f"{tequila_endpoint}/v2/search",
                headers=header,
                params=search
            )
            data = response.json()['data'][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                destination_city=data["cityTo"],
                destination_airport=data['flyTo'],
                out_date=data["route"][0]['local_departure'].split("T")[0],
                return_date=data["route"][-1]['local_departure'].split("T")[0],
                stop_overs=2,
                via_city=[data["route"][0]['cityTo'], data["route"][-1]['cityFrom']]

            )
            print(f"Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight.origin_airport} to "
                  f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")
        else:
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
