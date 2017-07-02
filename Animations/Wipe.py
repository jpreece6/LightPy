from LedAnimation import Animation, KeyFrame
from neopixel import *
import time
from random import randint

class WipeAnimation(Animation):

    def WipeDef(self, strip, kwargs):
        pos = kwargs['pos']
        ledColor = kwargs['col']
        delay = kwargs['delay']

        strip.setPixelColor(pos, ledColor)
        strip.show()
        time.sleep(delay/1000.0)

    def CalculateRange(self, direction=1, ledCount=0):
        if direction == 1:
            return range(ledCount)
        else:
            return range(ledCount, -1, -1)

    def Wipe(self, strip, direction=1):
        ledCount = strip.numPixels()
        workingRange = self.CalculateRange(direction, ledCount)

        for j in workingRange:
            frame1 = KeyFrame(self.WipeDef, strip, pos=j, col=Color(0,0,255), delay=40)
            self.AddFrame(frame1)
        return self

    def WipeRand(self, strip, direction=1):
        ledCount = strip.numPixels()
        workingRange = self.CalculateRange(direction, ledCount)

        for j in workingRange:
            frame1 = KeyFrame(self.WipeDef, strip, pos=j, col=Color(randint(0, 255), randint(0, 255), randint(0, 255)), delay=40)
            self.AddFrame(frame1)
        return self

    def __init__(self):
        Animation.__init__(self)