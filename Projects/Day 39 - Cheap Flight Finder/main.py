#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

dataManager = DataManager()
sheetData = dataManager.sheetData
flightSearch = FlightSearch()

# for entry in sheetData:
#     if entry["iataCode"] == "":
#         flightSearch.searchCity(entry["city"])
#         cityCode = flightSearch.cityCode
#         dataManager.updateIataCode(entry["id"], cityCode)

flightSearch.searchFlights("PAR", 300)
