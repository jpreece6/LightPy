import time
from neopixel import *

LED_COUNT = 21
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
LED_STRIP = ws.WS2811_STRIP_GRB

if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	try:
		for j in range(15):
			strip.setPixelColor(j, Color(0,0,0))

		UpdateBrightness(0)
		UpdateBrightness(50)
		UpdateBrightness(100)
		UpdateBrightness(150)
		UpdateBrightness(200)
		UpdateBrightness(220)
		UpdateBrightness(255)
	finally:
		for j in range(strip.numPixels()):
			strip.setPixelColor(j, Color(0,0,0))

def UpdateBrightness(strip, level, delay):
	strip.setBrightness(level)
	strip.show()
	time.sleep(delay)
