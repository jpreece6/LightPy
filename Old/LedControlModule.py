# TODO
# Add background color setting to be applied to all animations
# Make animations stackable (to play one after another)
# Create random selected animations to begin and end
# Modify animations to transition to and from default light color 
# Monitor time of day to control brightness and only switch on at "dark" times

import time
import ConfigReader
from neopixel import *
from blinker import signal
from random import randint

LED_COUNT = 31
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 200
LED_INVERT = False
LED_CHANNEL = 0
LED_STRIP = ws.WS2811_STRIP_GRB

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
animationComplete = signal("animationComplete")

def Setup():
	cfg = ConfigReader.GetConfig()
	LED_COUNT = cfg['leds']['count']
	LED_BRIGHTNESS = cfg['leds']['brightness']['default']
	strip.begin()
	SwitchOff()

def SwitchOff():
	for j in range(strip.numPixels()):
		strip.setPixelColor(j, Color(0,0,0))

	strip.show()

def SwitchOn():
	strip.setBrightness(180)
	strip.setPixelColor(1, Color(255, 0, 0))
	strip.show()

def DefaultDisplay():
	for j in range(strip.numPixels()):
		strip.setPixelColor(j, Color(100,100,100))
	strip.show()

def SetStripColor(color, brightness=180):
	for j in range(strip.numPixels()):
		strip.setPixelColor(j, color)
	strip.setBrightness(brightness)
	strip.show()

def SetBrightness(val):
	strip.setBrightness(val)
#	strip.show()
 
def Fade(color, step=1, startBright=180, endBright=0, transitionDelay=20):
	SetStripColor(color, startBright)
#	print transitionDelay
	time.sleep(transitionDelay/1000.0)
	for i in range(startBright, endBright, step):
		strip.setBrightness(i)
		time.sleep(transitionDelay/1000.0)
		strip.show()
	

def Pulse(color, iterations=1):
	for l in range(iterations):
		Fade(color, 1, 0, 180)
		time.sleep(100/1000.0)
		Fade(color, -1, 180, 0)
#	animationComplete.send()

def PulseColors(colors, maxBrightness=180, endState=1, delay=20, iterations=1): 
	for l in range(iterations):
		for j in colors[:-1]:
			Fade(j, 1, 0, maxBrightness, delay)
			Fade(j, -1, maxBrightness, 0, delay)
			time.sleep(100/1000.0)			
		else:
			Fade(colors[-1], 1, 0, maxBrightness, delay)

#	animationComplete.send()

def Wipe(color, direction=1, brightness=180, delay=30):
#	strip.setBrightness(brightness)
	workingRange = strip.numPixels()
	
	if direction == 1:
		workingRange = range(workingRange)
	else:
		workingRange = range(workingRange, -1, -1)

	for j in workingRange:
		strip.setPixelColor(j, color)
		strip.show()
		time.sleep(delay/1000.0)
		
def RandPos(colors, delay=20):
	active = [0] * strip.numPixels()
#	strip.setBrightness(180)	
	while 0 in active:
		target = randint(0, strip.numPixels() - 1)
		if (active[target] == 0):
			active[target] = 1
			strip.setPixelColor(target, colors[randint(0, len(colors) - 1)])
			time.sleep(delay/1000.0)
			strip.show()

def Bounce(color, startSize=4, speed=30, iterations=4, delay=30, add=0):
#	strip.setBrightness(180)
	size = startSize
	for i in range(iterations):
# Left
		for r in range(strip.numPixels()+size):
			if r <= strip.numPixels():
				strip.setPixelColor(r, color)
			if r >= size:
				strip.setPixelColor(r-size, Color(0,0,0))
			strip.show()
			time.sleep(speed/1000.0)
		
		size = startSize + add
		time.sleep(delay/1000.0)
# Right
		for l in range(strip.numPixels(), size*-1 , -1):
			if l <= strip.numPixels():
				strip.setPixelColor(l, color)
			if l >= 0 and l <= (strip.numPixels() - size):
				strip.setPixelColor(l+size, Color(0,0,0))
			strip.show()
			time.sleep(speed/1000.0)

def SetBlock(color, start=4, size=4):
#	strip.setBrightness(180)
	for j in range(size):
		strip.setPixelColor(start+j, color)
		strip.show()
	time.sleep(10/1000.0)

def Split(baseColor, color, speed=70):
#	strip.setBrightness(180)
	for j in range(strip.numPixels()):
		strip.setPixelColor(j, baseColor)
	strip.show()	

	for l in range(strip.numPixels()):
		strip.setPixelColor((strip.numPixels()/2)-l, color)
		strip.setPixelColor((strip.numPixels()/2)+l, color)
		strip.show()
		time.sleep(speed/1000.0)

