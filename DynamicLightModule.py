import AstroModule as astro
import time
import datetime
import math
from pytz import timezone 


MAX_BRIGHTNESS = 220
# UTC offset
PEAK_EVENING_TIME = datetime.datetime(2017, 1, 1, 17, 0, 0)
PEAK_MORNING_TIME = datetime.datetime(2017, 1, 1, 5, 0, 0)
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

	early_bound_rise = sunrise - BOUND_OFFSET
	early_bound_set = sunset - BOUND_OFFSET
	early_bound_eve_peak = PEAK_EVENING_TIME - BOUND_OFFSET
	early_bound_mor_peak = PEAK_MORNING_TIME - BOUND_OFFSET
	late_bound_eve_peak = PEAK_EVENING_TIME + BOUND_OFFSET
	
	eve_peak_end = PEAK_EVENING_TIME + PEAK_DURATION

#	print PEAK_EVENING_TIME
#	print sunrise
#	print sunset
#	print now
#	print early_bound_rise
#	print early_bound_set
#	print early_bound_eve_peak
#	print early_bound_mor_peak

	if now.time() > sunrise.time():
		# Sunset
		if now.time() >= PEAK_EVENING_TIME.time() and now.time() <= eve_peak_end.time():
 			return MAX_BRIGHTNESS
		elif now.time() >= early_bound_eve_peak.time() and now.time() < PEAK_EVENING_TIME.time():
			# Gradual increase until peak time 
			diff = now - PEAK_EVENING_TIME
			newVal = CalculateIncraseVal(diff.seconds)
			print newVal
		 
	else:
		# Sunrise
		print ""

def CalculateIncreaseVal(seconds):
	val = math.floor((seconds / 10) / 2)
	if (val > MAX_BRIGHTNESS):
		val = MAX_BRIGHTNESS
	elif val < 0:
		val = 0
	return val

def CalculateDecreaseVal(seconds):
	print ""

GetBrightness()
	
	
	
