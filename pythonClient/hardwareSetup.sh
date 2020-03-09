#! /bin/bash

# Make HardwareInit.py executeable 
chmod +x ./hardwareinit.py
# Update boot files with HardwareInit.py
cp ./hardwareinit.py /etc/init.d
# Make sure the script isn't already installed
update-rc.d -f hardwareinit.py remove
# Update the config file to run script at boot
update-rc.d hardwareinit.py defaults
