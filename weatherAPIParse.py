import requests
import json

# Parses DarkSky API request info given Latitude and Longitude information
class APIParse:
    # Enter Personal DARKSKY secret Key below
    key = ''

    # Constructor
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # URL Getter Method
    def getUrl(self):
        url = "https://api.darksky.net/forecast/" + self.key + "/" + str(self.lat) + "," + str(self.lon)
        return(url)

    # JSON Object Getter Method
    def getJSON(self):
        url = self.getUrl()
        weatherData = requests.get(url).json()
        return(weatherData)

    def getTimeZone(self):
        # Declare and init json object
        data = self.getJSON()

        timeZone = data['timezone']
        return(timeZone)

    # Returns a dict of Basic Weather Info
    def getBasicInfo(self):
        # declare and init json object
        data = self.getJSON()

        # Gather basic data
        sum = data['currently']['summary']
        precipChance = 100 * float(data['currently']['precipProbability'])
        temp = float(data['currently']['temperature'])
        humid = float(data['currently']['humidity'])
        windSpd = float(data['currently']['windSpeed'])
        uv = float(data['currently']['uvIndex'])

        # Create dict of basic info
        crucialInfo = {
            'Summary' : sum,
            'Precipitation Chance' : precipChance,
            'Temperature' : temp,
            'Humidity' : humid,
            'Wind Speed' : windSpd,
            'UV Index' : uv
        }

        return (crucialInfo)
        