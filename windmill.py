import RPi.GPIO as GPIO
import time


class Windmill(object):

	"""docstring for Windmill"""
	def __init__(self):
		super(Windmill, self).__init__()
		self.pin = 16
		self.pulse_time = 0.05
		self.break_time = .2
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.OUT)
		self.turn_off()

	def __del__(self):
		self.turn_off()
		GPIO.cleanup()

	def turn_on(self):
		GPIO.output(self.pin, GPIO.LOW) # start engine

	def turn_off(self):
		GPIO.output(self.pin, GPIO.HIGH) # stop engine

	# def turn_on_for_time(self, time):
	# 	self.turn_on()
	# 	time.sleep(time)
	# 	self.turn_off()

	def pulse(self, n):
		for x in range(n):
			# pulse
			self.turn_on()
			time.sleep(self.pulse_time)
			self.turn_off()

			time.sleep(self.break_time) # break before new pulse