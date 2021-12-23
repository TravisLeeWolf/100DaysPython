class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.flightList = []
        self.printout = ""
        self.notificationFlightList = []

    def sortFlightData(self, fromFlightResult):
        if fromFlightResult != "":
            fR = fromFlightResult
            # Sorts for the display
            availableFlight = [fR["cityTo"], fR["price"]]
            self.flightList.append(availableFlight)
            # Sorts for the notification
            forNotification = [fR["price"], fR["cityFrom"], fR["flyFrom"], fR["cityTo"], fR["flyTo"], fR["route"][0]["local_departure"], fR["route"][1]["local_departure"]]
            self.notificationFlightList.append(forNotification)

    def displayFlightList(self):
        for item in self.flightList:
            self.printout += f"{item[0]}: £{item[1]}\n"
        print(self.printout)