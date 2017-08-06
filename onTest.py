import time

from neopixel import *
from random import randint

# LED strip configuration:
LED_COUNT      = 62      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

def Pulse(strip, color, iterDelay=100, transitionDelay=20, iterations=8):
	for j in range(strip.numPixels()):
		strip.setPixelColor(j, color)
	strip.setBrightness(255)
	strip.show()

try:

	if __name__ == '__main__':
		# Create NeoPixel object with appropriate configuration.
		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
		# Intialize the library (must be called once before other functions).
		strip.begin()

		print ('Press Ctrl-C to quit.')
		while True:
	#		Random(strip)
			Pulse(strip, Color(255, 255, 255))
except KeyboardInterrupt:
	print "End"
