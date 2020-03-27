import servo_simulator as s
import co2_sensor_simulator as co2
import time


def save_data(oxygen, angle):
	print("writing to file", oxygen, angle)

def main():
	servo = s.Servo()
	# servo.SetAngle(10)
	sensor = co2.Co2Sensor()
	treshold = 400
	# sensor.sense()


	# 1. Read sensor
	# 2. act on sensor data -> servo
	# 3. save data to file
	# 4. pause for a while

	while True:
		oxygen = sensor.sense()
		if oxygen > treshold:
			servo.SetAngle(30)
		else:
			servo.SetAngle(10)

		save_data(oxygen, servo.getRotation())

		# time.sleep(300) # 5 min
		time.sleep(5) # 5 seconds

if __name__ == '__main__':
	main()