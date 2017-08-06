import yaml
from subprocess import call

#Path = "/tmp/config.yaml"
Path = "/home/pi/LightPy/config.yaml"

def GetConfig() :
	with open(Path, 'r') as ymlfile:
		try:
			return yaml.load(ymlfile)
		except yaml.YAMLError as exc:
			print (exc)

def Dump(data):
	OpenFs()
	with open(Path, "w") as f:
		try:
			yaml.dump(data, f)
		except yaml.YAMLError as exc:
			print (exc)
	CloseFs()


def OpenFs():
	call(["/bin/bash", "-i", "-c", "rw"])

def CloseFs():
	call(["/bin/bash", "-i", "-c", "ro"])
