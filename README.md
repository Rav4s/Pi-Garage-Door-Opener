# Pi-Garage-Door-Opener
Contains Python script, schematics, and additional information from the youtube video at https://youtu.be/An7KQbmUnhs. The install.sh file can automate all of the tasks involved in this project, including installing python3, installing bottlepy, making the directory, pulling the latest version of the python script, and editing the /etc/rc.local file to run on startup.
## How to run install.sh ##
### Make sure system is up to date: ###
`sudo apt update && sudo apt upgrade -y`
### Get the latest version of the script ###
`wget https://raw.githubusercontent.com/Rav4s/Pi-Garage-Door-Opener/master/install.sh`
### Add execute permissions ###
`chmod +x install.sh`
### Run the script and follow the terminal prompts ###
`./install.sh`
## Accessing the website ##
After the reboot, you can access your garage door at http://serverip:1234/login. The default password is xxxx. You can change this by editing the line that says pswd="xxxx" to whatever password you'd like to have.
