from StoppableThread import StoppableThread
from threading import Thread
from blinker import signal

class KeyFrame:
	
	def __init__(self, animationFunc, strip, **kwargs):
		self.Animation = animationFunc
		self.strip = strip
		self.kwargs = kwargs

	def Play(self):
		self.Animation(self.strip, self.kwargs)

class Animation:
	
	def AnimationThread(self):
		for k in self.KeyFrames:
			k.Play()
		self.AnimationComplete.send()

	def __init__(self):
		self.AnimationComplete = signal('AnimationComplete')
		self.KeyFrames=[]
		self.InternalThread = Thread(target=self.AnimationThread)
	
	def AddFrame(self, frame):
		self.KeyFrames.append(frame)

	def Play(self):
		self.InternalThread.start()

	def Stop(self):
		self.InternalThread.join()

	def WaitUntilComplete(self):
		self.InternalThread.join()
