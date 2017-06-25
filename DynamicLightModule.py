# Remove peak time consider sunset times

import AstroModule as astro
import time
import datetime
import math
from pytz import timezone 


MAX_BRIGHTNESS = 220
DEFAULT_BRIGHTNESS = 80
# UTC offset
PEAK_EVENING_TIME = datetime.datetime.today().replace(hour=20, minute=30, second=0)
PEAK_MORNING_TIME = datetime.datetime.today().replace(hour=5, minute=0, second=0)
LOCATION = "Stroud UK"

PrevBrightness = 0

PEAK_DURATION = datetime.timedelta(minutes=30)
BOUND_OFFSET = datetime.timedelta(hours=1,minutes=30)

def GetBrightness():
	global PrevBrightness
	london = timezone("Europe/London")

	brightness = 1
	sunrise = astro.GetSunrise(LOCATION)
	sunset = astro.GetSunset(LOCATION)
	now = datetime.datetime.utcnow()	
	midnight = (datetime.datetime.today() + datetime.timedelta(days=1)).replace(hour=1, minute=0, second=0)
	
	early_bound_rise = sunrise - BOUND_OFFSET
	early_bound_set = sunset - BOUND_OFFSET
	early_bound_eve_peak = PEAK_EVENING_TIME - BOUND_OFFSET
	early_bound_mor_peak = PEAK_MORNING_TIME - BOUND_OFFSET
	late_bound_eve_peak = PEAK_EVENING_TIME + BOUND_OFFSET
	
	eve_peak_end = PEAK_EVENING_TIME + PEAK_DURATION

#	print midnight
	print PEAK_EVENING_TIME
#	print sunrise
#	print sunset
	print now
#	print early_bound_rise
#	print early_bound_set
	print early_bound_eve_peak
#	print early_bound_mor_peak

	if now.time() > sunrise.time() and now < midnight:
		# Sunset
		if now.time() >= PEAK_EVENING_TIME.time() and now.time() <= eve_peak_end.time():
 			return MAX_BRIGHTNESS
		elif now.time() >= early_bound_eve_peak.time() and now.time() < PEAK_EVENING_TIME.time():
			# Gradual increase until peak time 
			diff = PEAK_EVENING_TIME - now
			newVal = CalculateIncreaseVal(diff.seconds)
			print diff.seconds
			return newVal
		elif now.time() > eve_peak_end.time() and now.time() <= late_bound_eve_peak.time():
			# Gradual decrease until end of late bound
			diff = late_bound_eve_peak - now
			newVal = CalculateDecreaseVal(diff.seconds)
			print diff.seconds
			return newVal			
		else:
			# All other cases return
			return DEFAULT_BRIGHTNESS
		 
	else:
		# Sunrise
		print "sss"

def CalculateIncreaseVal(seconds):
	val = ((((seconds * -1) / 10) / 2) + 270)
	if (val > MAX_BRIGHTNESS):
		val = MAX_BRIGHTNESS
	elif val < 0:
		val = 0
	return val

def CalculateDecreaseVal(seconds):
	val = ((seconds / 10) / 2)
	if (val > MAX_BRIGHTNESS):
		val = MAX_BRIGHTNESS
	elif val < 0:
		val = 0
	return val

print GetBrightness()
	
	
	
