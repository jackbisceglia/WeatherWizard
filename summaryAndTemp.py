from geocodeAPIParse import cityToAbsolute
from weatherAPIParse import APIParse

def getNeededInfo(city):

    # initialize CityToAbsolute object and use getter methods
    absolute = cityToAbsolute(city)

    lat = absolute.getLatittude()
    lon = absolute.getLongitude()

    # initialize APIParse object and use info getter methods
    parsedObj = APIParse(lat, lon)

    basicInfoDict = parsedObj.getBasicInfo()
    wantedTimeZone = parsedObj.getTimeZone()
    wantedTimeZone = wantedTimeZone.replace('_', ' ')

    # Extract necessary info
    summ = basicInfoDict['Summary']
    temp = basicInfoDict['Temperature']
    precip = basicInfoDict['Precipitation Chance']

    # Format to dict and return for use in Flask app
    necessaryInfo = {
        'Outlook' : summ,
        'Temp' : temp,
        'Precip' : precip,
        'TimeZone' : wantedTimeZone
        }

    return(necessaryInfo)