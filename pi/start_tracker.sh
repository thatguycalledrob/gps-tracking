#!bin bash

# This script is designed to be run by the PI on startup
# to install it (assuming rasbian here) use the following
# in the pi's bash:
#   sudo nano /etc/rc.local

# add the following lines (assuming start_tacker):
#   git clone https://github.com/thatguycalledrob/gps-tracking.git /home/pi/Desktop
#   sudo /home/pi/Desktop/start_tracker.sh &

# this will now get the latest version of of the gps tracking script, then 
echo "hello world"
sudo python3