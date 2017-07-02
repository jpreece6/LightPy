from neopixel import *
import time

def BaseLight(strip, kwargs):
    for j in range(strip.numPixels()):
        strip.setPixelColor(j, Color(0,0,255))
    strip.show()