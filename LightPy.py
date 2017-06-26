import HardwareModule
import RPi.GPIO as GPIO
import time
import os
import sys

try:
	HardwareModule.Setup()
	while 1:
		HardwareModule.MotionModule.ReadPin()
		time.sleep(10/1000.0)
except KeyboardInterrupt:
	print "End"
finally:
	HardwareModule.LedReset()
	time.sleep(1)
	GPIO.cleanup()
	print "Clean"
#	sys.exit(0)
	os._exit(0)
	
	
