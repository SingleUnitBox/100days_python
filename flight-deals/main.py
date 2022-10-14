#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
data_manager = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()

# sheet_data = data_manager.get_destination_data()
sheet_data = [{'city': 'Bali', 'iataCode': 'DPS', 'lowestPrice': 1000, 'id': 3},
              {'city': 'Heraklion', 'iataCode': 'HER', 'lowestPrice': 100, 'id': 2}]
ORIGIN_CITY_IATA = "LON"
#
# if sheet_data[0]["iataCode"] == "":
#     from flight_search import FlightSearch
#     flight_search = FlightSearch()
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row['city'])
#     print(sheet_data)
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.search_cheap_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow.strftime("%d/%m/%Y"),
        to_time=six_month_from_today.strftime("%d/%m/%Y")
    )
    if flight is None:
        continue
    if flight.price < destination['lowestPrice']:
        # print(f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
        #       f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")
        notification.send_email(notification.get_user(), flight)
        print("email sent")

