import ephem
import ConfigReader
from Geo import GeoLocator

class AstroCalculator:

    def GetSunrise(self):
        return self.observer.next_rising(self.sun).datetime()

    def GetSunset(self):
        return self.observer.next_setting(self.sun).datetime()

    def __init__(self):
        self.geoLocator = GeoLocator()
        self.observer = ephem.Observer()
        self.observer.lat = self.geoLocator.Latitude
        self.observer.lon = self.geoLocator.Longitude
        self.sun = ephem.Sun()
        self.sun.compute(self.observer)

    Sunset = property(GetSunset)
    Sumrise = property(GetSunrise)