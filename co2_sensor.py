import mh_z19 # requires sudo

class Co2Sensor(object):

	"""docstring for Co2Sensor"""
	def __init__(self):
		super(Co2Sensor, self).__init__()
		
	def sense(self):
		val = -1
		try:
			val = mh_z19.read_all()['co2']
		except Exception as e:
			print("Could not read sensor", e)
		print("Sensor: ", val)
		return val