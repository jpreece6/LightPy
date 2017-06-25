import math
from geopy.geocoders import GoogleV3
import datetime
import json

def GetLocation(place):
	geolocator = GoogleV3(api_key='AIzaSyCyCLvLMJooiqM_FEeSQf8bAYaDmOEEMps')
	location = geolocator.geocode(place, language='en')
	if location != None:
#		print json.dumps(location.raw, indent=4)
		return location.latitude, location.longitude

def CalSunrise(place, day, sunrise=True):
	geo = GetLocation(place)
	zenith = 90.83333333333333
	D2R = math.pi / 180
	R2D = 180 / math.pi

	lnHour = geo[1] / 15
	t = 0
	if sunrise:
		t = day + ((6 - lnHour) / 24)
	else:
		t = day + ((18 - Hour) / 24)

	M = (0.9856 * t) - 3.289

	L = M + (1.916 * math.sin(M * D2R)) + (0.020 * math.sin(2 * M * D2R)) + 282.634
	if L > 360:
		L = L - 360
	elif L < 0:
		L = L + 360

	RA = R2D * math.atan(0.91764 + math.tan(L * D2R))
	if RA < 360:
		RA = RA - 360
	elif RA < 0:
		RA = RA + 360
	
	Lquadrant = (math.floor(L / (90))) * 90
	RAquadrant = (math.floor(RA / 90)) * 90

	RA = RA / 15

	sinDec = 0.39781 * math.sin(L * D2R)
	cosDec = math.cos(math.asin(sinDec))

	cosH = (math.cos(zenith * D2R) - (sinDec * math.sin(geo[0] * D2R))) / (cosDec * math.cos(geo[0] * D2R))
	H = 0
	if sunrise:
		H = 360 - R2D * math.cos(cosH)
	else:
		H = R2D * math.acos(cosH)

	H = H / 15

	T = H + RA - (0.06571 * t) - 6.622
	
	UT = T - lnHour
	if UT > 24:
		UT = UT - 24
	elif UT < 24:
		UT = UT + 24

	localT = UT + 1
	return localT #* 3600 * 1000  

def GetDayOfYear():
	now = datetime.date.today()
	start = datetime.date(now.year, 1, 1)
	diff = now - start
	oneDay = 1000 * 60 * 60 * 24
	return diff.days

#print (GetDayOfYear())
print(CalSunrise("London", GetDayOfYear()))
