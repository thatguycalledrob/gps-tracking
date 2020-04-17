#!/bin/bash

# This script is designed to be run by the PI on startup
# and does the following:
#   1. updates the gps script to latest master version
#   2. runs this bash script to start the tracker script
# to install it (assuming rasbian here) use the following

# if you have not already, run:
#    cd ~/Desktop
#    git clone https://github.com/thatguycalledrob/gps-tracking.git

# in the pi's bash:
#   sudo nano /etc/rc.local

# add the following line (assuming you have already cloned):
#   sudo /home/pi/Desktop/gps-tracking/pi/start_tracker.sh &

# this will now get the latest version of of the gps tracking script, then

sleep 15; # sleep allows system to fully boot

cd /home/pi/Desktop/gps-tracking

# debug output to check that all is well
timestamp=$(date +%s)
echo "[DEBUG] beginning execution at time : $(timestamp)" >> latest.txt
chmod 755 latest.txt

# commenting out this line in the short term
# git remote update

export GPS_URL="https://gps-listener-lcn55j3ska-ew.a.run.app"

# again, some subprocess spawning
sudo python3 /home/pi/Desktop/gps-tracking/pi/start_tracker.py &
echo "[DEBUG] begun python script : $(timestamp)" >> latest.txt
wait