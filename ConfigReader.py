import yaml

#Path = "/tmp/config.yaml"
Path = "/home/pi/LightPy/config.yaml"

def GetConfig() :
	with open(Path, 'r') as ymlfile:
		try:
			return yaml.load(ymlfile)
		except yaml.YAMLError as exc:
			print (exc)

def Dump(data):
	with open(Path, "w") as f:
		try:
			yaml.dump(data, f)
		except yaml.YAMLError as exc:
			print (exc)