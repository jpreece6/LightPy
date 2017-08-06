from shutil import copyfile
from subprocess import call
import datetime

def Write(msg):
	f = open('/tmp/light.log', 'a+')
	f.write(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S") + " - ")
	f.write(msg)
	f.write('\n')
	f.close()

def Save():
	call(['/bin/bash', '-i', '-c', 'rw'])
	copyfile('/tmp/light.log', '/home/pi/logs/light.log')
	call(['/bin/bash','-i','-c','ro'])
	
