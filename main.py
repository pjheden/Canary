import windmill as wm
import co2_sensor as co2
import time
import datetime
import sys

def logprint(printstr):
	print(printstr)
	sys.stdout.flush()

def save_data(oxygen, angle):
	now = datetime.datetime.now().isoformat()
	logprint("timestamp: " + str(now))
	f = open("./www/static/data.csv","a")
	f.write(now + "," + str(oxygen) + "," + str(angle) + "\n")
	f.close()

def main():
	windmill = wm.Windmill()
	sensor = co2.Co2Sensor()
	treshold = 900

	while True:
		oxygen = sensor.sense()
		if oxygen > treshold:
			windmill.pulse(10)
		else:
			pass

		save_data(oxygen, -1)

		# time.sleep(300) # 5 min
		time.sleep(100) # 5 seconds

if __name__ == '__main__':
	main()
	# save_data(10, 90)
