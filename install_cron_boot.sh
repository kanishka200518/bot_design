#!/bin/bash
echo "Installing Crontab Auto-Boot Fallback..."

# The command we want to run on boot
# Sleep 15s to ensure Wi-Fi and Camera are initialized before Python starts
CRON_CMD="@reboot sleep 15 && cd /home/botdesign/AutonomousRover && sudo /usr/bin/python3 main.py > /home/botdesign/AutonomousRover/rover.log 2>&1"

# Check if it already exists to avoid duplicates
(sudo crontab -l 2>/dev/null | grep -q "$CRON_CMD") || {
    # It doesn't exist, append it
    (sudo crontab -l 2>/dev/null; echo "$CRON_CMD") | sudo crontab -
}

echo "Crontab Fallback Installed!"
echo "The robot will now automatically run the code ~15 seconds after you plug in the battery."
echo "If you ever want to see any errors or print logs, you can read the log file by typing:"
echo "cat /home/botdesign/AutonomousRover/rover.log"
