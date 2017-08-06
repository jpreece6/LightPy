from LedAnimation import Animation, KeyFrame
from neopixel import *
from random import randint
import time

class BounceAnimation(Animation):

    def Left(self, strip, kwargs):
        speed = kwargs['delay']
        color = kwargs['color']
        size = kwargs['size']

        for r in range(size*-1, (strip.numPixels()+size)+2, 1):
			if r <= strip.numPixels():
				strip.setPixelColor(r, color)
			if r >= size:
				strip.setPixelColor(r-size, Color(0,0,0))
			strip.show()
			time.sleep(speed/1000.0)

    def Right(self, strip, kwargs):
        speed = kwargs['delay']
        color = kwargs['color']
        size = kwargs['size']

        for l in range(strip.numPixels(), ((size+1)*-1) , -1):
			if l <= strip.numPixels():
				strip.setPixelColor(l, color)
			if l >= (size*-1) and l <= (strip.numPixels() - size):
				strip.setPixelColor(l+size, Color(0,0,0))
			strip.show()
			time.sleep(speed/1000.0)

    def Bounce(self, strip, iterations=2):
        for j in range(iterations):
            frame1 = KeyFrame(self.Left, strip, delay=40, color=Color(0,0,255), size=4)
            frame2 = KeyFrame(self.Right, strip, delay=40, color=Color(0,0,255), size=4)
            self.AddFrame(frame1)
            self.AddFrame(frame2)
        frame3 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=self.max_brightness, col=self.base_color, delay=20)
        self.AddFrame(frame3)
        return self

    def BounceRand(self, strip, iterations=4):
        color = Color(randint(0, 255), randint(0, 255), randint(0, 255))
        for j in range(iterations):
            frame1 = KeyFrame(self.Left, strip, delay=40, color=color, size=4)
            frame2 = KeyFrame(self.Right, strip, delay=40, color=color, size=4)
            self.AddFrame(frame1)
            self.AddFrame(frame2)

        frame3 = KeyFrame(self.FadeDef, strip, stBright=0, edBright=self.max_brightness, col=self.base_color, delay=20)
        self.AddFrame(frame3)
        return self

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

    def __init__(self, max_brightness=30, base_color=Color(30,30,90)):
        self.max_brightness = max_brightness
        self.base_color = base_color
        Animation.__init__(self)