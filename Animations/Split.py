from LedAnimation import Animation, KeyFrame
from neopixel import *
import time
from random import randint

class SplitAnimation(Animation):

    def StepDef(self, strip, kwargs):
        speed = kwargs['delay']
        color = kwargs['color']

        strip.setBrightness(self.max_brightness)
        for l in range(strip.numPixels()):
            strip.setPixelColor((strip.numPixels()/2)-l, color)
            strip.setPixelColor((strip.numPixels()/2)+l, color)
            strip.show()
            time.sleep(speed/1000.0)

    def SplitIn(self, strip):
        frame1 = KeyFrame(self.StepDef, strip, delay=50, color=self.base_color)
        self.AddFrame(frame1)
        return self

    def SplitOut(self, strip):
        frame1 = KeyFrame(self.StepDef, strip, delay=50, color=Color(0,0,0))
        self.AddFrame(frame1)
        return self

    def SplitRandIn(self, strip):
        color = Color(randint(0, 255), randint(0, 255), randint(0, 255))
        frame1 = KeyFrame(self.StepDef, strip, delay=50, color=color)
        self.AddFrame(frame1)
        frame1 = KeyFrame(self.StepDef, strip, delay=50, color=self.base_color)
        self.AddFrame(frame1)
        return self

    def SplitRandOut(self, strip):
        color = Color(randint(0, 255), randint(0, 255), randint(0, 255))
        frame1 = KeyFrame(self.StepDef, strip, delay=50, color=color)
        self.AddFrame(frame1)
        frame2 = KeyFrame(self.StepDef, strip, delay=50, color=Color(0,0,0))
        self.AddFrame(frame2)
        return self

    def __init__(self, max_brightness, base_color):
        self.max_brightness = max_brightness
        self.base_color = base_color
        Animation.__init__(self)