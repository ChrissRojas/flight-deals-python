# Flight Price Tracker

Flight Price Tracker is used to track the prices of a given list of locations. 
Various APIs are used to gain the flight data as well as to update the google spreadsheet.


## Requirements

If you do plan on using this program the following is needed:

- The Twilio API for sending SMS (Don't Worry this has a free trial to test out without the need to update)
- Kiwi API for flight data (Also free)
- Sheety API for updating API (Be careful this only has 200 free requests)
- The Requests Library (High Level Library which uses URLLib for requests) (Download using PIP)
- SMTP Library for sending emails. (Part of the python standard library) 

## The Program itself

The Data Manager Class will handle two sets of data:
- The Flight data itself
- The User data if there are people who signed up to get notifications.

The Data Manager class will then send the data to the google sheets and update when necessary.
You're probably wondering why I didn't use a database for this... Well...
This is a Capstone Project for the 100 Days Challenge. The requirements was meant to use a spreadsheet.
We're not making an extensive application here where a database is needed. The database would only have
two tables and a spreadsheet/csv file would be easy to query.

Flight Data Class:
You can treat this as a dataclass. Mainly there to make it easier to retrieve data after a query from a
Flight_search Query.

Flight Search Class:
In Summary this searches for flight data using the Tequila api. Now if you look at the Tequila API... particularly for it's search part.
You'll see why the flight data class is needed. There's just so much data that the query returns from this search 
that it makes it a pain just to index within the dictionary.

Notification Manager:
The notification manager has the functionality to send sms or emails to those who have signed up.
This uses the Twilio API to send the sms messages and also uses the smtp library built into python.

## Known Issues:
- Can search for flights with more than or equal to 1 stopover, but cannot be printed out. Flight_data returns null as a result when in fact there is a flight.
- Due to the previous point. One of the destination points is printed out but does not sdkf
- Program can be a bit slow. Not entirely sure if this is due to the Tequila api.

## Improvements:
Apart from the Known issues list.

- Database could be implemented to store different users and Tkinter for data entry.
- Concurrency/Parallel. Data entry and querying can completely be decoupled and ran in parallel.
- Choice of either SMS and Email notifications.




