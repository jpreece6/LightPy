import HardwareModule
import time
import os
import sys
import ConfigReader


if __name__ == '__main__':

	cfg = ConfigReader.GetConfig()
	onTime = cfg['strip']['less_than_time']
	endTime = cfg['strip']['greater_than_time']
	h = HardwareModule.HardwareController()
	startTime = time.time()
	prevTime = startTime

	try:

		while 1:
			nowTime = time.strftime('%H:%M')
			startTime = time.time()

			# update config every minute
			if (startTime - prevTime > 60):
				cfg = ConfigReader.GetConfig()
				onTime = cfg['strip']['less_than_time']
				endTime = cfg['strip']['greater_than_time']
				prevTime = startTime

			if (nowTime <= onTime):
				h.Update()
			elif (nowTime >= endTime):
				h.Update()
			

			time.sleep(500/1000.0)
	except Exception, e:
		print str(e)
	finally:
		h.Exit()
		print ("Clean")
		os._exit(0)
		
	
