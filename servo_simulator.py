import RPi.GPIO as GPIO
import time


class Servo(object):

	"""docstring for Servo"""
	def __init__(self):
		super(Servo, self).__init__()
		self.angle = 0
		self.servoPIN = 17
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.servoPIN, GPIO.OUT)
		self.pwm = GPIO.PWM(self.servoPIN, 50) #setup PWM on pin at 50Hz
		self.pwm.start(0)

	def __del__(self):
		self.pwm.stop()
		GPIO.cleanup()

	def SetAngle(self, angle):
		duty = angle / 18 + 2
		GPIO.output(self.servoPIN, True)
		pwm.ChangeDutyCycle(duty)
		time.sleep(1)
		GPIO.output(self.servoPIN, False)
		pwm.ChangeDutyCycle(0)
		self.angle = angle
		print("rotated to ", angle)


	def getRotation(self):
		return self.angle