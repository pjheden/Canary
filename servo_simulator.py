

class Servo(object):

	"""docstring for Servo"""
	def __init__(self):
		super(Servo, self).__init__()
		self.angle = 0
	
	def rotateTo(self, deg):
		print("rotated to ", deg)
		self.angle = deg

	def getRotation(self):
		return self.angle