import MotionModule
import LedController
import ConfigReader
import time, datetime
from neopixel import *
from blinker import signal
from threading import Timer
import random

class HardwareController:

    def Triggered(self):
        self.LastMotion = time.time()

        if self.AnimationIsRunning == False and self.TimoutLatch == False and self.EndLatch == False:
            self.AnimationIsRunning = True
            self.TimoutLatch = True
            self.LedController.Off()
            
            if (self.cfg['start_animation'] == 'Random'):
                choice = random.choice(self.LedController.StartAnimations.keys())
            else:
                choice = self.cfg['start_animation']

            self.LedController.StartAnimations[choice].Play()
            
            self.TimoutTimer = Timer(self.cfg['motion']['timeout'], self.UpdateLatch, ())
            self.TimoutTimer.start()

    def AnimationComplete(self, sender):
        self.AnimationIsRunning = False
        self.EndLatch = False

    def Update(self):
        detected = self.MotionSensor.ReadPin()
        if detected:
            self.Triggered()

    def UpdateLatch(self):
        now = time.time()
        diff = now - self.LastMotion
        # Difference in seconds
        if (diff >= 6):
            if (self.cfg['end_animation'] == 'Random'):
                choice = random.choice(self.LedController.EndAnimations.keys())
            else:
                choice = self.cfg['end_animation']

            self.LedController.EndAnimations[choice].Play()
            self.TimoutLatch = False
            self.EndLatch = True
        else:
            self.TimoutTimer = Timer(self.cfg['motion']['timeout'], self.UpdateLatch, ())
            self.TimoutTimer.start()

    def LedReset(self):
        self.LedController.StopAnimation()

    def Exit(self):
        self.TimoutTimer.cancel()
        self.TimoutTimer = Timer(self.cfg['motion']['timeout'], self.UpdateLatch, ())
        self.LedController.Off()

    def __init__(self):
        self.cfg = ConfigReader.GetConfig()
        self.MotionSensor = MotionModule.PIRSensor()
        #self.MotionSensor.SignalMotion.connect(self.Triggered)
        self.LedController = LedController.LedController()
        self.LedController.AnimationCompleteEvent.connect(self.AnimationComplete)
        self.AnimationIsRunning = False
        self.TimoutTimer = Timer(self.cfg['motion']['timeout'], self.UpdateLatch, ())
        self.TimoutLatch = False
        self.EndLatch = False
        self.LastMotion = time.time()

    def __del__(self):
        self.MotionSensor.SignalMotion.disconnect(self.Triggered)