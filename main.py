import servo_simulator as s
import co2_sensor_simulator as co2


def save_data(oxygen, angle):
	print("writing to file", oxygen, angle)

def main():
	servo = s.Servo()
	# servo.rotateTo(10)
	sensor = co2.Co2Sensor()
	# sensor.sense()


	# 1. Read sensor
	# 2. act on sensor data -> servo
	# 3. save data to file
	# 4. pause for a while

	while True:
		oxygen = sensor.sense()
		if oxyen > treshold:
			servo.rotateTo(30)
		else:
			servo.rotateTo(10)

		save_data(oxygen, servo.getRotation())

		time.sleep(300000) # 5 min

if __name__ == '__main__':
	main()