from LedAnimation import Animation, KeyFrame
from neopixel import *
import time
from random import randint

class WipeAnimation(Animation):

    def WipeDef(self, strip, kwargs):
        pos = kwargs['pos']
        ledColor = kwargs['col']
        delay = kwargs['delay']

        strip.setBrightness(self.max_brightness)
        strip.setPixelColor(pos, ledColor)
        strip.show()
        time.sleep(delay/1000.0)

    def CalculateRange(self, direction=1, ledCount=0):
        if direction == 1:
            return range(ledCount)
        else:
            return range(ledCount, -1, -1)

    def WipeIn(self, strip, direction=1, color=Color(0,0,255)):
        ledCount = strip.numPixels()
        workingRange = self.CalculateRange(direction, ledCount)

        for j in workingRange:
            frame1 = KeyFrame(self.WipeDef, strip, pos=j, col=color, delay=40)
            self.AddFrame(frame1)
        return self

    def WipeOut(self, strip, direction=1, color=Color(0,0,255)):
        ledCount = strip.numPixels()
        workingRange = self.CalculateRange(direction, ledCount)
        
        for j in workingRange:
            frame2 = KeyFrame(self.WipeDef, strip, pos=j, col=Color(0,0,0), delay=40)
            self.AddFrame(frame2)
        return self

    def WipeRandIn(self, strip, direction=1, iterations=1):
        ledCount = strip.numPixels()
        workingRange = self.CalculateRange(direction, ledCount)

        for x in range(iterations):
            for j in workingRange:
                frame1 = KeyFrame(self.WipeDef, strip, pos=j, col=Color(randint(0, 255), randint(0, 255), randint(0, 255)), delay=40)
                self.AddFrame(frame1)
        for j in workingRange:
                frame1 = KeyFrame(self.WipeDef, strip, pos=j, col=self.base_color, delay=40)
                self.AddFrame(frame1)
        return self

    def WipeRandOut(self, strip, direction=1, iterations=1):
        ledCount = strip.numPixels()
        workingRange = self.CalculateRange(direction, ledCount)

        for x in range(iterations):
            for j in workingRange:
                frame1 = KeyFrame(self.WipeDef, strip, pos=j, col=Color(randint(0, 255), randint(0, 255), randint(0, 255)), delay=40)
                self.AddFrame(frame1)
        for j in workingRange:
                frame1 = KeyFrame(self.WipeDef, strip, pos=j, col=Color(0,0,0), delay=40)
                self.AddFrame(frame1)
        return self

    def __init__(self, max_brightness=30, base_color=Color(30,30,90)):
        self.max_brightness = max_brightness
        self.base_color = base_color
        Animation.__init__(self)