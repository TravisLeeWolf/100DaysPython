class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.flightList = []

    def sortFlightData(self, fromFlightResult):
        if fromFlightResult != "":
            availableFlight = [fromFlightResult["cityTo"], fromFlightResult["price"]]
            self.flightList.append(availableFlight)

    def displayFlightList(self):
        for item in self.flightList:
            print(f"{item[0]}: £{item[1]}")