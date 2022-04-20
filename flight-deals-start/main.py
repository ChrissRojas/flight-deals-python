from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

flight_sheet = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()
FROM_IATA = "LON"


def main():
    if flight_sheet.sheet_data["prices"][0]["iataCode"] == "":
        for iata in flight_sheet.sheet_data["prices"]:
            if len(iata["iataCode"]) == 0:
                iata_response = flight_search.get_dest_code(iata["city"])
                iata["iataCode"] = iata_response
                sheet_row = {
                    "price": {
                        "iataCode": iata_response
                    }
                }
            flight_sheet.update_row(iata["id"], sheet_row)
    pprint(flight_sheet.sheet_data)
    tomorrow = datetime.now() + timedelta(days=1)
    six_months = datetime.now() + timedelta(days=(6 * 30))

    for places in flight_sheet.sheet_data["prices"]:
        flight = flight_search.check_flights(
            frm_city_code=FROM_IATA,
            destination_city_code=places["iataCode"],
            from_time=tomorrow,
            to_time=six_months
        )
        if flight is None:
            continue
        if flight.price < places["lowestPrice"]:
            message = f"Alert! £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to" \
                      f" {flight.destination_city}-{flight.destination_airport}, from {flight.leave_date} to {flight.return_date}"
            if flight.stopovers > 0:
                message += f"\nFlight has {flight.stopovers} stop over, via {flight.viacity}"
                print(flight.viacity)
            link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.leave_date}*{flight.origin_airport}.{flight.return_date}"
            notification.send_emails(flight_sheet.user_data, message, link)


if __name__ == "__main__":
    main()
