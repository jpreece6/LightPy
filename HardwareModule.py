import MotionModule
from blinker import signal

def Setup():
    MotionModule.Setup()
    MotionModule.sigMotion.connect(MotionEvent)

def Destruct():
    MotionModule.sigMotion.disconnect(MotionEvent)

def MotionEvent():
    print ""
