from threading import Thread

class KeyFrame:
	
	Animation = 0

	def __init__(self, animationFunc):
		Animation = animationFunc

	def Play():
		print("Play")

class Animation:
	KeyFrames = []
	AnimationThread = Thread()	

	def __init__(self) :
	
	def AddFrame(frame):
		KeyFrames.append(frame)

	def Play():
		for k in KeyFrames:
			k.Play()

	def Stop():
		AnimationThread.

	def 
