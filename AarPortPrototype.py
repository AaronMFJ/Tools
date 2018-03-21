import urllib.request


print("Welcome to Aviation Weather Prototype")


userAirport = input("Enter airport ID ICAO. For example, KRDU: ")
userAirport = str(userAirport)
#url = "https://aviationweather.gov/metar/data?ids=" + userAirport + "&format=raw&date=0&hours=0"
url = "https://aviationweather.gov/adds/metars/index?submit=1&station_ids=" + userAirport + "&chk_metars=on&chk_tafs=on&hoursStr=2&std_trans=translated"
print(url) #test the url

#parse the airport page
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
results = response.read()
data = results.decode('utf-8')
airportResult = 0


for x in data.splitlines():
        if userAirport.upper() in x:
           # airportResult = (x.split(",")[0]) this one works
            airportResult = (x.split("/tr"))
            break
print(airportResult)



# This is v1 results
# for x in data.splitlines():
#         if userAirport.upper() in x:
#             print(x.split("<")[0])


