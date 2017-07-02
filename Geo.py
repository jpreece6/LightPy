from geopy.geocoders import GoogleV3
import ConfigReader

class GeoLocator:

    def __init__(self):
        self.cfg = ConfigReader.GetConfig()

        if self.cfg['geo']['enabled'] == True:
            location = self.GetLocation()
            self.Longitude = location[1]
            self.Latitude = location[0]
        else:
            self.Longitude = self.cfg['geo']['default_longitude']
            self.Latitude = self.cfg['geo']['default_latitude']

    def GetLocation(self):
        ApiKey = self.cfg['geo']['api_key']
        place = self.cfg['geo']['location']
        if ApiKey != None:
            google = GoogleV3(api_key=ApiKey)
            location = google.geocode(place, language='en')
            if location != None:
                return str(location.latitude), str(location.longitude)
    
    def GetLongitude(self):
        return self.Longitude

    def GetLatitude(self):
        return self.Latitude

    Longitude = property(GetLongitude)
    Latitude = property(GetLatitude)