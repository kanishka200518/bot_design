#!/bin/bash
echo "Installing dependencies for the Raspberry Pi Autonomous Rover..."

# Update package lists
sudo apt-get update
sudo apt-get install -y python3-pip python3-opencv libzbar0

# Install Python requirements globally so the sudo cron script can access them
# The --break-system-packages flag is required on Ubuntu 24.04 when installing globally outside a venv
sudo pip3 install --upgrade setuptools wheel --break-system-packages
sudo pip3 install -r requirements.txt --break-system-packages || echo "Vanilla requirements failed, attempting specialized AI packages..."

# Install a Python 3.11/3.12 compatible tflite-runtime wheel if it failed from requirements.txt
sudo pip3 install tflite-runtime --extra-index-url https://google-coral.github.io/py-repo/ --break-system-packages || sudo pip3 install tensorflow-cpu-aws --break-system-packages || sudo pip3 install tensorflow --break-system-packages

echo "Setup Complete!"
echo "Make sure I2C / Camera / GPIO is enabled in sudo raspi-config"
echo "To run the rover: python3 main.py"
