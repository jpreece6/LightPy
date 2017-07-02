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

    def Build(self, strip):
        colours = self.GenerateRandomColours()
        frame1 = KeyFrame(self.BuildDef, strip, colours=colours, delay=30)
        self.AddFrame(frame1)
        return self

    def __init__(self):
        Animation.__init__(self)