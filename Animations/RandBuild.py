from LedAnimation import Animation, KeyFrame
from neopixel import *
import time
from random import randint

class RandBuildAnimation(Animation):

    def BuildDef(self, strip, kwargs):
        active = [0] * strip.numPixels()
        colours = kwargs['colours']
        delay = kwargs['delay']

        while 0 in active:
            target = randint(0, strip.numPixels() - 1)
            if (active[target] == 0):
                active[target] = 1
                strip.setPixelColor(target, colours[randint(0, len(colours) - 1)])
                time.sleep(delay/1000.0)
                strip.show()

    def GenerateRandomColours(self, numColours=4):
        colours = []
        for j in range(numColours):
            colours.append(Color(randint(0, 255), randint(0, 255), randint(0, 255)))
        return colours

    def BuildIn(self, strip, color=Color(30,30,90)):
        #colours = self.GenerateRandomColours()
        frame1 = KeyFrame(self.BuildDef, strip, colours=color, delay=30)
        self.AddFrame(frame1)
        return self

    def __init__(self, max_brightness=30, base_color=Color(30,30,90)):
        self.max_brightness = max_brightness
        self.base_color = base_color
        Animation.__init__(self)