#!/bin/bash

sudo apt -y install python3
sudo cp /bin/python3 /bin/python
pip install psycopg2-binary
sudo apt install -y nginx

git config --global user.email "seanfahey10@gmail.com"
git config --global user.name "Sean Fahey"

# Enable and start nginx service
sudo systemctl enable nginx
sudo systemctl start nginx

# Navigate to your project directory
cd ~/mm-chess/chess7

# Optionally, activate your virtual environment here
# source your_virtual_env/bin/activate

# Install project dependencies
pip3 install -r requirements.txt

# Run Gunicorn to serve your Django application in detached mode
#gunicorn chess5.wsgi:application --bind 127.0.0.1:8000 --daemon
python manage.py runserver 127.0.0.1:8000
# Place the Nginx configuration file in the sites-available directory
# Replace 'your_nginx_config' with the actual path to your Nginx config file
sudo rm /etc/nginx/sites-enabled/mm-chess.conf
sudo cp ~/mm-chess/mm-chess.conf /etc/nginx/sites-available/mm-chess.conf

# Create a symbolic link to enable the site
sudo ln -s /etc/nginx/sites-available/mm-chess.conf /etc/nginx/sites-enabled/

# Test the Nginx configuration
sudo nginx -t

# Restart Nginx for changes to take effect
sudo systemctl restart nginx

