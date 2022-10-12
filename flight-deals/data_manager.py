import requests
sheety_enpoint = "https://api.sheety.co/945910ca7ee851937e94aa321f5e90a0/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_enpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            sheet_input = {
                "price": {
                    'iataCode': city["iataCode"]
                }
            }
            sheet_response = requests.put(
                url=f"{sheety_enpoint}/{city['id']}",
                json=sheet_input
            )
            print(sheet_response.text)


