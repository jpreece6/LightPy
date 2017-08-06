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
        frame1 = KeyFrame(self.FadeDef, strip, stBright=self.max_brightness, edBright=-1, col=self.base_color, delay=20)
        self.AddFrame(frame1)
        return self
    
    def FadeIn(self, strip):
        frame1 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=self.max_brightness, col=self.base_color, delay=20)
        self.AddFrame(frame1)
        return self

    def FadeColoursIn(self, strip, colors, iterations=1):
        for x in range(iterations):
            for j in colors:
                frame1 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=self.max_brightness, col=j, delay=20)
                frame2 = KeyFrame(self.FadeDef, strip, stBright=self.max_brightness, edBright=-1, col=j, delay=20)
                self.AddFrame(frame1)
                self.AddFrame(frame2)
        frame3 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=self.max_brightness, col=self.base_color, delay=20)
        self.AddFrame(frame3)
        return self

    def FadeColoursOut(self, strip, colors, iterations=1):
        frame = KeyFrame(self.FadeDef, strip, stBright=self.max_brightness, edBright=0, col=self.base_color, delay=20)
        self.AddFrame(frame)
        for x in range(iterations):
            for j in colors:
                frame1 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=self.max_brightness, col=j, delay=20)
                frame2 = KeyFrame(self.FadeDef, strip, stBright=self.max_brightness, edBright=-1, col=j, delay=20)
                self.AddFrame(frame1)
                self.AddFrame(frame2)
        return self

    def FadeRand(self, strip, iterations=1):
        for j in range(iterations):
            color = Color(randint(0, 255), randint(0, 255), randint(0, 255))
            frame1 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=self.max_brightness, col=color, delay=20)
            frame2 = KeyFrame(self.FadeDef, strip, stBright=self.max_brightness, edBright=-1, col=color, delay=20)
            self.AddFrame(frame1)
            self.AddFrame(frame2)

        return self

    def FadeRandIn(self, strip, iterations=1):
        for j in range(iterations):
            color = Color(randint(0, 255), randint(0, 255), randint(0, 255))
            frame1 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=self.max_brightness, col=color, delay=20)
            frame2 = KeyFrame(self.FadeDef, strip, stBright=self.max_brightness, edBright=-1, col=color, delay=20)
            self.AddFrame(frame1)
            self.AddFrame(frame2)

        frame3 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=self.max_brightness, col=self.base_color, delay=20)
        self.AddFrame(frame3)

        return self

    def FadeRandOut(self, strip, iterations=1):
        frame = KeyFrame(self.FadeDef, strip, stBright=self.max_brightness, edBright=0, col=self.base_color, delay=20)
        self.AddFrame(frame)
        for j in range(iterations):
            color = Color(randint(0, 255), randint(0, 255), randint(0, 255))
            frame1 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=self.max_brightness, col=color, delay=20)
            frame2 = KeyFrame(self.FadeDef, strip, stBright=self.max_brightness, edBright=-1, col=color, delay=20)
            self.AddFrame(frame1)
            self.AddFrame(frame2)

        return self

    def __init__(self, max_brightness=30, base_color=Color(30,30,90)):
        self.max_brightness = max_brightness
        self.base_color = base_color
        Animation.__init__(self)