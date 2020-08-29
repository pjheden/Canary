# Canary
In previous times miners brought canary birds down to the mines to warn for gass.
The small lugns made the birds collapse way before the miners, effectively giving
a warning that toxic gasses are in the air.

## Connections
pins etc

## Start service that runs the program automatically
https://www.raspberrypi.org/documentation/linux/usage/systemd.md

## Systemd service
### Initialize
#### Move to right place
sudo cp myscript.service /etc/systemd/system/myscript.service
#### Start service
sudo systemctl start myscript.service
#### Autostart on boot
sudo systemctl enable myscript.service
#### Update script
Upon updating the script you need to stop then start the service again
for it to take effect.

### Read logs
journalctl -u canary.service -f

## Run the program
sudo python3 main.py

## Angles
The backside is where the cable enter the servo
* 0: short side to the left
* 90: short side backward
* 180: short side to the right 

## Timestamp notes
* 2020-03-28T21:44:57.179936 close the window
* 2020-03-28T23:11:48.681456 open window
