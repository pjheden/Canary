import windmill as wm
import button as btn
import co2_sensor as co2
import thread
import time
import datetime
import sys

def logprint(printstr):
	print(printstr)
	sys.stdout.flush()

def save_data(oxygen, temperature):
	now = datetime.datetime.now().isoformat()
	logprint("timestamp: " + str(now))
	f = open("./www/static/data.csv","a")
	f.write(now + "," + str(oxygen) + "," + str(temperature) + "\n")
	f.close()

def listen_to_button(button, windmill):
	while True:
		if button.is_pressed():
			windmill.turn_on()
		else:
			windmill.turn_off()

		time.sleep(0.1)

def main():
	windmill = wm.Windmill()
	button = btn.Button()
	sensor = co2.Co2Sensor()
	treshold = 900

	thread.start_new_thread( listen_to_button, (button, windmill, ) )

	while True:
		sensor_reading = sensor.sense()
		oxygen = sensor_reading['co2']
		if oxygen > treshold:
			windmill.pulse(10)
		else:
			pass

		save_data(oxygen, sensor_reading['temperature'])

		# time.sleep(300) # 5 min
		time.sleep(100) # 5 seconds

if __name__ == '__main__':
	main()
