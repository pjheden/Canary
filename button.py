import RPi.GPIO as GPIO
import time


class Button(object):

	"""docstring for Button"""
	def __init__(self):
		super(Button, self).__init__()
		self.pin = 12
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


	def __del__(self):
		GPIO.cleanup()

	def is_pressed(self):
		return GPIO.input(self.pin) == GPIO.HIGH