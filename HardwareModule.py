import MotionModule
import LedController
import ConfigReader
import time, datetime
from neopixel import *
from blinker import signal
from threading import Timer
import random

# Flag animations as ON or OFF animations to display an active color after and ON animation and switch off leds after a OFF animation

class HardwareController:

    def Triggered(self, sender):
        self.LastMotion = time.time()
        #print self.LastMotion
        if self.AnimationIsRunning == False and self.TimoutLatch == False and self.EndLatch == False:
            self.LedController.Off()
            choice = random.choice(self.LedController.StartAnimations.keys())
            self.LedController.StartAnimations[choice].Play()
            self.AnimationIsRunning = True
            self.TimoutLatch = True
            self.TimoutTimer = Timer(self.cfg['motion']['timeout'], self.UpdateLatch, ())
            self.TimoutTimer.start()
            #self.TimoutScheduler.enter(self.cfg['motion']['timeout'], 1, self.UpdateLatch, ())
            #self.TimoutScheduler.run()

    def AnimationComplete(self, sender):
        self.AnimationIsRunning = False
        self.EndLatch = False

    def Update(self):
        detected = self.MotionSensor.ReadPin()
        #if detected:
        #    self.Triggered()

    def UpdateLatch(self):
        now = time.time()
        diff = now - self.LastMotion
        print diff
        if (diff >= 6):
            choice = random.choice(self.LedController.EndAnimations.keys())
            self.LedController.EndAnimations[choice].Play()
            self.TimoutLatch = False
            self.EndLatch = True
        else:
            self.TimoutTimer = Timer(self.cfg['motion']['timeout'], self.UpdateLatch, ())
            self.TimoutTimer.start()

    def Exit(self):
        self.TimoutTimer.cancel()
        self.TimoutTimer = Timer(self.cfg['motion']['timeout'], self.UpdateLatch, ())
        self.LedController.Off()

    def __init__(self):
        self.cfg = ConfigReader.GetConfig()
        self.MotionSensor = MotionModule.PIRSensor()
        self.MotionSensor.SignalMotion.connect(self.Triggered)
        self.LedController = LedController.LedController()
        self.LedController.AnimationCompleteEvent.connect(self.AnimationComplete)
        self.AnimationIsRunning = False
        self.TimoutTimer = Timer(self.cfg['motion']['timeout'], self.UpdateLatch, ())
        self.TimoutLatch = False
        self.EndLatch = False
        self.LastMotion = time.time()

    def __del__(self):
        self.MotionSensor.SignalMotion.disconnect(self.Triggered)