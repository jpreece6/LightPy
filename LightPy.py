import HardwareModule
import RPi.GPIO as GPIO
import time

try:
	HardwareModule.Setup()
	while 1:
		time.sleep(10)
finally:
	HardwareModule.LedReset()
	GPIO.cleanup()

	
	
