#!/bin/bash

echo "This script will install the bottlepy web server and allow you to control and monitor the state of your smart garage door opener."
sleep 1
echo "Before running this script, make sure you've configured your network and done a sudo apt update && sudo apt upgrade, so your system is up to date."
sleep 1
echo "The default password is xxxx. YOU MUST CHANGE THIS AS IT IS VERY INSECURE."
sleep 1
read -r -p "Press y to acknowledge and continue running the script. [y/N] " response

if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
then
    echo "Installing python3 and pip3..."
    sudo apt -y install python3 python3-pip
    echo "Making directory..."
    mkdir garagedoor && cd garagedoor
    sleep 0.5
    echo "Installing Bottlepy..."
    pip3 install bottle
    sleep 0.5
    echo "Getting latest py file..."
    wget https://raw.githubusercontent.com/Rav4s/Pi-Garage-Door-Opener/master/Python_script_for_garage_door.py
    sleep 0.5
    echo "Editing /etc/rc.local for auto startup..."
    sudo sed -i 'x; ${s/.*/python3 /home/pi/Python_script_for_garage_door.py &/;p;x}; 1d' /etc/rc.local
    sleep 0.5
    echo "Successful install! Rebooting in 5 seconds!"
    sleep 5
    sudo shutdown -r now
else
    echo "Bye!"
    exit 1
fi

exit 0
