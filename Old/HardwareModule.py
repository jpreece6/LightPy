import MotionModule
import LedControlModule
import DynamicLightModule
from threading import Timer
from neopixel import *
from random import randint

ResetRequested = 0
LedState = 0
TimeoutTimer = 0
Timeout = 60.0

def Setup():
	global TimeoutTimer
	TimeoutTimer = Timer(Timeout, LedStop, ())
	MotionModule.Setup()
	MotionModule.sigMotion.connect(LedStart)
	LedControlModule.Setup()
	LedControlModule.animationComplete.connect(LedAnimationComplete)

def LedStart(sender):
#	TimeoutTimer = Timer(15.0, LedStop, ())
	global TimeoutTimer
	TimeoutTimer.cancel()
	
	if ResetRequested == 1:
		return

	TimeoutTimer = Timer(Timeout, LedStop, ())
	TimeoutTimer.start()	
		
	global LedState
	if LedState == 0:
		LedState = 1
		brightness = DynamicLightModule.GetBrightness() 
		
		if brightness == 0:
			return # Switch off as it is day time

		colors = [Color(0,255,0),Color(0,0,255),Color(100,100,100)]	
		ranColor = [Color(randint(0,255),randint(0,255),randint(0,255)),Color(randint(0,255),randint(0,255),randint(0,255))]

		delay = 20
		if brightness > 140:
			delay = ((brightness * -1) / 2) + 130
		else:
			delay = (brightness * -1) + 130

		print delay
		LedControlModule.SetBrightness(brightness)
#		LedControlModule.PulseColors(colors, brightness, delay=delay)
#		LedControlModule.Wipe(Color(44,0,44), 2)
#		LedControlModule.RandPos(ranColor)
		LedControlModule.Bounce(Color(22,33,120), 2, 50, 20, 30, 1)
#		LedControlModule.SetBlock(Color(100,0,100))
#		LedControlModule.Split(Color(0,0,0),Color(255,0,0))
		
def LedStop():
	print("OFF")
	global LedState
	LedState = 0
	LedControlModule.Wipe(Color(0,0,0))

def LedReset():
	MotionModule.sigMotion.disconnect(LedStart)
	global ResetRequested
	ResetRequested = 1
	print("Reset")
	global LedState
	LedState = 0
	LedControlModule.Wipe(Color(0,0,0))

def LedAnimationComplete(sender):
	LedControlModule.DefaultDisplay()
	




	
