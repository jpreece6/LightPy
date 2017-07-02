from LedAnimation import Animation, KeyFrame
from neopixel import *
import time
from random import randint

class SplitAnimation(Animation):

    def StepDef(self, strip, kwargs):
        speed = kwargs['delay']
        color = kwargs['color']

        for l in range(strip.numPixels()):
            strip.setPixelColor((strip.numPixels()/2)-l, color)
            strip.setPixelColor((strip.numPixels()/2)+l, color)
            strip.show()
            time.sleep(speed/1000.0)

    def Split(self, strip):
        color = Color(0, 0, 255)
        frame1 = KeyFrame(self.StepDef, strip, delay=50, color=color)
        self.AddFrame(frame1)
        return self

    def SplitRand(self, strip):
        color = Color(randint(0, 255), randint(0, 255), randint(0, 255))
        frame1 = KeyFrame(self.StepDef, strip, delay=50, color=color)
        self.AddFrame(frame1)
        return self

    def __init__(self):
        Animation.__init__(self)