class FlightData:
    def __init__(self, price, from_city, from_airport, to_city, to_airport, leave_date, return_date,
                 stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = from_city
        self.origin_airport = from_airport
        self.destination_city = to_city
        self.destination_airport = to_airport
        self.leave_date = leave_date
        self.return_date = return_date
        self.stopovers = stop_overs
        self.viacity = via_city
