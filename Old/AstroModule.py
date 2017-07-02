import ephem
from datetime import *
from pytz import timezone
from geopy.geocoders import GoogleV3
import ConfigReader

ApiKey = None
Latitude = "51.500"
Longitude = "-0.126236" 

def Setup():
	global ApiKey
	global Latitude
	global Longitude

	cfg = ConfigReader.GetConfig()
	useGeo = cfg['geoLocation']['enabled']

	if (useGeo):
		ApiKey = cfg['geoLocation']['api_key']

	Latitude = str(cfg['geoLocation']['latitude'])
	Longitude = str(cfg['geoLocation']['longitude'])

def GetLocation(place):
	if ApiKey != None:
		geolocator = GoogleV3(api_key=ApiKey)
		location = geolocator.geocode(place, language='en')
		if location != None:
			return str(location.latitude), str(location.longitude)
	else:
		return Latitude, Longitude

def GetObserver(geo, elevation=60):
	obs = ephem.Observer()
	obs.lat = geo[0]
	obs.lon = geo[1]
	obs.elevation = elevation
	return obs

def SetupSun(place):
	geo = GetLocation(place)
	observer = GetObserver(geo)
	sun = ephem.Sun()
	sun.compute(observer)	
	return sun, observer

def GetSunrise(place="London UK", timez='Europe/London', returnTwilight=False):
	sun = SetupSun(place)
	london = timezone(timez)
	return  london.normalize(london.localize(sun[1].previous_rising(sun[0], use_center=returnTwilight).datetime()))

def GetSunset(place="London UK", timez='Europe/London', returnTwilight=False):
	sun = SetupSun(place)
	london = timezone(timez)
	return london.normalize(london.localize(sun[1].next_setting(sun[0], use_center=returnTwilight).datetime()))
	
