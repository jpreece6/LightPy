import sys
sys.path.append('/home/pi/LightPy/Animations')
from neopixel import *
from LedAnimation import Animation
from blinker import signal
from Fade import FadeAnimation
from Wipe import WipeAnimation
from RandBuild import RandBuildAnimation
from Split import SplitAnimation
from Bounce import BounceAnimation
import ConfigReader

class LedController:

    def __init__(self, useConfig=True, count=0, pin=18, frq=800000, dma=5, brightness=200, invert=False, channel=0):
        
        if (useConfig):
            self.cfg = ConfigReader.GetConfig()
            self.count = self.cfg['strip']['count']
            self.pin = self.cfg['strip']['pin']
            self.frq = self.cfg['strip']['frq']
            self.dma = self.cfg['strip']['dma']
            self.brightness = self.cfg['strip']['brightness']
            self.invert = self.cfg['strip']['invert']
            self.channel = self.cfg['strip']['channel']
        else:
            self.count = count
            self.pin = pin
            self.frq = frq
            self.dma = dma
            self.brightness = brightness
            self.invert = invert
            self.channel = channel
            
        self.type = ws.WS2811_STRIP_GRB
        self.strip = Adafruit_NeoPixel(self.count, self.pin, self.frq, self.dma, self.invert, self.brightness, self.channel, ws.WS2811_STRIP_GRB)
        self.strip.begin()
        self.RegisterAnimations()

    def RegisterAnimations(self):
        self.Animations = {}
        self.Animations['FadeOut'] = FadeAnimation().FadeOut(self.strip)
        self.Animations['FadeIn'] = FadeAnimation().FadeIn(self.strip)
        self.Animations['Fade'] = FadeAnimation().Fade(self.strip, [Color(0,0,255), Color(255,0,0)])
        self.Animations['FadeRand'] = FadeAnimation().FadeRand(self.strip)
        self.Animations['Wipe'] = WipeAnimation().Wipe(self.strip, 0)
        self.Animations['WipeRand'] = WipeAnimation().WipeRand(self.strip)
        self.Animations['RandBuild'] = RandBuildAnimation().Build(self.strip)
        self.Animations['Split'] = SplitAnimation().Split(self.strip)
        self.Animations['SplitRand'] = SplitAnimation().SplitRand(self.strip)
        self.Animations['Bounce'] = BounceAnimation().Bounce(self.strip)
        self.Animations['BounceRand'] = BounceAnimation().BounceRand(self.strip)

        for v in self.Animations.itervalues():
            v.AnimationComplete.connect(self.AnimationComplete)

    def AnimationComplete(self, sender):
        print "End"

    def On(self):
        for j in range(self.strip.numPixels()):
            self.strip.setPixelColor(j, Color(0,0,255))
        self.strip.setBrightness(90)
        self.strip.show()

    def Off(self):
        for j in range(self.strip.numPixels()):
            self.strip.setPixelColor(j, Color(0,0,0))
        self.strip.show()

    def StopAnimation(self):
        self.Animator.Stop()