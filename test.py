#import AstroModule
#import DynamicLightModule

#AstroModule.Setup()
#result = AstroModule.GetSunrise("Stroud UK")

#DynamicLightModule.Setup()
#result = DynamicLightModule.GetBrightness()

from LedController import LedController
from BrightnessController import BrightnessController
import ConfigReader
import time

b = BrightnessController()
print b.UpdateBrightness()

#print ConfigReader.GetConfig()
#bri = BrightnessController()
#bri.UpdateBrightness()
#print ConfigReader.GetConfig()


#cont = LedController(useConfig=False, count=31, brightness=40)
#cont.Animations['FadeRand'].Play()
#cont.On() 
#time.sleep(15)
#cont.Animations['WipeRand'].Play()
#cont.StopAnimation()
#cont.Off()
