import  MotionModule
import LedControlModule
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
		colors = [Color(0,255,0),Color(0,0,255),Color(100,100,100)]	
		ranColor = [Color(randint(0,255),randint(0,255),randint(0,255)),Color(randint(0,255),randint(0,255),randint(0,255))]
		LedControlModule.PulseColors(colors)
#		LedControlModule.Wipe(Color(44,0,44), 2)
#		LedControlModule.RandPos(ranColor)
#		LedControlModule.Bounce(Color(22,33,120), 2, 50)
#		LedControlModule.SetBlock(Color(100,0,100))
#		LedControlModule.Split(Color(0,0,0),Color(255,0,0))
		
def LedStop():
	print("OFF")
	global LedState
	LedState = 0
	#LedControlModule.SwitchOff()
	LedControlModule.Wipe(Color(0,0,0))

def LedReset():
	global ResetRequested
	ResetRequested = 1
	print("Reset")
	global LedState
	LedState = 0
	LedControlModule.Wipe(Color(0,0,0))

def LedAnimationComplete(sender):
	LedControlModule.DefaultDisplay()
	




	
