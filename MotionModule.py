import RPi.GPIO as GPIO
from blinker import signal

PIR_PIN = 7
sigMotion = signal('motion')

def Setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(PIR_PIN, GPIO.IN)
#	GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=Motion)

def Motion(PIR_PIN):
	sigMotion.send()
#	print ("Motion")

def ReadPin():
	if GPIO.input(PIR_PIN):
		Motion(PIR_PIN)
