#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

dataManager = DataManager()
sheetData = dataManager.sheetData
flightSearch = FlightSearch()
flightData = FlightData()
emailSender = NotificationManager()

for entry in sheetData:
    if entry["iataCode"] == "":
        flightSearch.searchCity(entry["city"])
        cityCode = flightSearch.cityCode
        dataManager.updateIataCode(entry["id"], cityCode)


for entry in sheetData:
    flightSearch.searchFlights(destinationCode=entry["iataCode"], maxPrice=entry["lowestPrice"])
    flightData.sortFlightData(flightSearch.flightData)


flightData.displayFlightList()
emailSender.getFlightList(flightData.notificationFlightList)
emailSender.sendMail()