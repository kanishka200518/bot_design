#!/bin/bash
echo "Installing Autonomous Rover Auto-Boot Service..."

# Assuming you transferred the folder to /home/pi/AutonomousRover
# Edit the paths in rover.service if different.

sudo cp rover.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable rover.service
sudo systemctl start rover.service

echo "Service Installed and Enabled!"
echo "The robot will now automatically start the code (and the web dashboard) whenever you turn on the battery."
echo "To check the background log status, you can type: sudo journalctl -fu rover.service"
echo "To stop the robot manually: sudo systemctl stop rover.service"
