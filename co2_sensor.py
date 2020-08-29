import mh_z19 # requires sudo

class Co2Sensor(object):

	"""docstring for Co2Sensor"""
	def __init__(self):
		super(Co2Sensor, self).__init__()
		
	def sense(self):
		val = {'co2': -1, 'temperature': -1}
		try:
			val = mh_z19.read_all()
			# check that both values we care about are there
			print(val)
			val['co2']
			val['temperature']
		except Exception as e:
			print("Could not read sensor", e)
			val = {'co2': -1, 'temperature': -1}
		print("Sensor: ", val)
		return val
