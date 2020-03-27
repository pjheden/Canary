import random

class Co2Sensor(object):

	"""docstring for Co2Sensor"""
	def __init__(self):
		super(Co2Sensor, self).__init__()
		self.angle = 0
	
	def sense(self):
		val = random.random() * 600 + 200
		print("Co2: ", val)