import RPi.GPIO as GPIO
from blinker import signal

PIR_PIN = 7

class PIRSensor:

	def ReadPin(self):
		if GPIO.input(PIR_PIN):
			self.SignalMotion.send()
			return True
		return False

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(PIR_PIN, GPIO.IN)
		self.SignalMotion = signal('motion')

	def __del__(self):
		GPIO.cleanup()

#def Setup():
#	GPIO.setmode(GPIO.BCM)
#	GPIO.setup(PIR_PIN, GPIO.IN)
#	GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=Motion)

#def Motion(PIR_PIN):
#	sigMotion.send()
#	print ("Motion")

#def ReadPin():
#	if GPIO.input(PIR_PIN):
#		Motion(PIR_PIN)
