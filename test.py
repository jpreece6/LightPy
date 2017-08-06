from LedController import LedController
from BrightnessController import BrightnessController
import ConfigReader
import time
import MotionModule
import HardwareModule

try:

    h = HardwareModule.HardwareController()
    h.Triggered()
    while 1:
        #h.Update()
        time.sleep(10/1000)

except KeyboardInterrupt:
    h.Exit()
    print "End"
