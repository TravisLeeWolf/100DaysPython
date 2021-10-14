from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from signup_manager import SignupManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
signup_manager = SignupManager()

addUser = input("Do you want to sign up for the mailing list? (Type 'Y' to sign up): ")
if addUser.upper() == "Y":
    signup_manager.requestUserDetails()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    try:
        flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
        stopovers=0
        )
        if flight.price < destination["lowestPrice"]:
            notification_manager.send_email(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.",
                link=f"https://www.kayak.com/flights/{flight.origin_airport}-{flight.destination_airport}/{flight.out_date}/{flight.return_date}?sort=bestflight_a"
            )
    except AttributeError:
        try:
            flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            stopovers=1
            )
            if flight.price < destination["lowestPrice"]:
                notification_manager.send_email(
                    message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.{flight.stopover}"
                )
        except AttributeError:
            continue
