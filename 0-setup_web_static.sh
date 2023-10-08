#!/usr/bin/env bash
# prepare nginx for static deployement
# text colors
green='\033[1;32m'
orange='\033[1;38;5;208m'

cprint() {
  local color=$1
  local text=$2
  local reset='\033[0m'
  echo -e "${color}${text}${reset}"
}

cprint "$green" "Good Moring I would like to update && upgrade and Installing Nginx... so bring snaks"

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

cprint "$green" "Nginx installed"
cprint "$green" "Creating folder for your static web and Configuring Nginx..."

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
# our basic test index.html file
config=\
"
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"
echo "$config" | sudo tee /data/web_static/releases/test/index.html

# creating symbolic link to index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# change ownership of /data/
sudo chown -hR ubuntu:ubuntu /data/

# update the Nginx config to serve the content of our basic html
cprint "$orange" "[ ! ] Configuring Nginx..."
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

cprint "$green" "[ * ] Nginx configured"
