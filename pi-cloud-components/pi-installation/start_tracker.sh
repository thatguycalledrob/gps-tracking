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
#   sudo /home/pi/Desktop/gps-tracking/pi-cloud-components/pi-installation/start_tracker.sh &

# this will now get the latest version of of the gps tracking script, then

sleep 30; # sleep allows system to fully boot. Important!


cd ~/Desktop/gps-tracking/pi-cloud-components/pi-installation

# debug output to check that all is well
timestamp=$(date +%s)
echo "[DEBUG] beginning execution at time : $(timestamp)" >> latest.txt
chmod 755 latest.txt

# commenting out this line in the short term
# git pull

# install the latest swagger generated library
cd swaggerlib
sudo python3 setup.py install

# fork a process with the gps running on it
cd ..
timestamp=$(date +%s)
echo "[DEBUG] beginning python script : $(timestamp)" >> latest.txt
sudo python3 gps.py &

# spew out some more debug logs here..
timestamp=$(date +%s)
echo "[DEBUG] begun python script : $(timestamp)" >> latest.txt
wait