import ephem
from datetime import *
from pytz import timezone
from geopy.geocoders import GoogleV3

def GetLocation(place):
	geolocator = GoogleV3(api_key='AIzaSyCyCLvLMJooiqM_FEeSQf8bAYaDmOEEMps')
	location = geolocator.geocode(place, language='en')
	if location != None:
		return location.latitude, location.longitude

def GetObserver(geo, elevation=60):
	#print geo[0]
	#print geo[1]
	obs = ephem.Observer()
	obs.lat = str(geo[0])
	obs.lon = str(geo[1])
	obs.elevation = elevation
	return obs

def GetSunrise(place, returnTwilight=False):
	geo = GetLocation(place)
	observer = GetObserver(geo)
	sun = ephem.Sun()
	sun.compute(observer)	
	london = timezone('Europe/London')
	return  london.normalize(london.localize(observer.previous_rising(sun, use_center=returnTwilight).datetime()))

def GetSunset(place, returnTwilight=False):
	geo = GetLocation(place)
	observer = GetObserver(geo)	
	sun = ephem.Sun()
	sun.compute(observer)
	london = timezone('Europe/London')
	return london.normalize(london.localize( observer.next_setting(sun, use_center=returnTwilight).datetime()))

#print GetSunset("Stroud UK")
	
