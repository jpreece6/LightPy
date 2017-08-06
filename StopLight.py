from LedControl import *

if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()
    for j in range(strip.numPixels()):
        strip.setPixelColor(j, Color(0,0,0))
    strip.show()
    print "OFF"