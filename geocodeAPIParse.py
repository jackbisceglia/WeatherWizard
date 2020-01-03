from opencage.geocoder import OpenCageGeocode as ocg

class cityToAbsolute:
    # Enter Personal OPENCAGE secret Key below
    openCageKey = ''

    # Constructor takes city paramter to use for geocoding
    def __init__(self, cityAndCountry):
        self.city = cityAndCountry

    # Getter method for geoCoder object
    def absoluteDict(self):
        # Creates instance
        geoCoder = ocg(self.openCageKey)
        query = self.city
        result = geoCoder.geocode(query)
        absoluteDict = result[0]['geometry']
        return(absoluteDict)

    # Getter method for Lattitude
    def getLatittude(self):
        latLon = self.absoluteDict()
        return(latLon['lat'])

    # Getter Method for Longitude
    def getLongitude(self):
        latLon = self.absoluteDict()
        return(latLon['lng'])    