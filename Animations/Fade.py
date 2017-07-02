from LedAnimation import Animation, KeyFrame
from neopixel import *
from random import randint
import time
import Common

class FadeAnimation(Animation):
    def FadeDef(self, strip, kwargs):
        startBright = kwargs['stBright']
        endBright = kwargs['edBright']
        ledColor = kwargs['col']
        delay = kwargs['delay']
        step = 1

        if (startBright > endBright):
            step = -1

        #strip.setBrightness(0)
        for j in range(strip.numPixels()):
            strip.setPixelColor(j, ledColor)

        for i in range(startBright, endBright, step):
            strip.setBrightness(i)
            time.sleep(delay/1000.0)
            strip.show()

    def FadeOut(self, strip):
        frame1 = KeyFrame(self.FadeDef, strip, stBright=180, edBright=-1, col=Color(0,0,255), delay=20)
        self.AddFrame(frame1)
        return self
    
    def FadeIn(self, strip):
        frame1 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=180, col=Color(0,0,255), delay=20)
        self.AddFrame(frame1)
        return self

    def Fade(self, strip, colors):
        for j in colors:
            frame1 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=180, col=j, delay=20)
            frame2 = KeyFrame(self.FadeDef, strip, stBright=180, edBright=-1, col=j, delay=20)
            self.AddFrame(frame1)
            self.AddFrame(frame2)
        
        return self

    def FadeRand(self, strip):
        color = Color(randint(0, 255), randint(0, 255), randint(0, 255))
        frame1 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=180, col=color, delay=20)
        frame2 = KeyFrame(self.FadeDef, strip, stBright=180, edBright=-1, col=color, delay=20)
        self.AddFrame(frame1)
        self.AddFrame(frame2)

        return self
    
    def __init__(self):
        Animation.__init__(self)