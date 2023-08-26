#!/bin/bash

sudo apt -y update
sudo apt -y install python3 python3-pip
sudo apt -y install nginx

# Start Nginx
sudo service nginx start

# Navigate to your project directory
cd ~/mm-chess/chess7

# Setup Python Environment
python3 -m venv venv
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# If you're going to use PostgreSQL
pip install psycopg2

# Nginx setup
# Assuming you're appending configuration, not removing all
sudo cp ~/mm-chess/mm-chess.conf /etc/nginx/sites-available/

# Create a symbolic link to enable the site
sudo ln -s /etc/nginx/sites-available/mm-chess.conf /etc/nginx/sites-enabled/

# Check and reload Nginx
sudo nginx -t
sudo service nginx reload

# Setup Gunicorn systemd service
echo "[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=username
Group=groupname
WorkingDirectory=/path/to/your/project
ExecStart=/path/to/your/project/venv/bin/gunicorn --bind localhost:8000 chess5.wsgi:application

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/gunicorn.service

# Start Gunicorn service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
