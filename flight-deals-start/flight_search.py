import requests
from flight_data import FlightData
from pprint import pprint


class FlightSearch:
    tequila_epoint = "https://tequila-api.kiwi.com"
    tequila_key = "YOUR-KEY"
    tq_qry = "locations/query"

    def get_dest_code(self, city_name) -> str:
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{self.tequila_epoint}/{self.tq_qry}",
                                params=query, headers={"apikey": self.tequila_key})
        return response.json()["locations"][0]["code"]

    def check_flights(self, frm_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": self.tequila_key}

        query = {
            "fly_from": frm_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=f"{self.tequila_epoint}/v2/search", params=query, headers=headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=f"{self.tequila_epoint}/v2/search", params=query, headers=headers)
            try:
                data = response.json()["data"][0]
            except IndexError:
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    from_city=data["route"][0]["cityFrom"],
                    from_airport=data["route"][0]["flyFrom"],
                    to_city=data["route"][1]["cityTo"],
                    to_airport=data["route"][1]["flyTo"],
                    leave_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.destination_city}: £{flight_data.price}")
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                from_city=data["route"][0]["cityFrom"],
                from_airport=data["route"][0]["flyFrom"],
                to_city=data["route"][0]["cityTo"],
                to_airport=data["route"][0]["flyTo"],
                leave_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
