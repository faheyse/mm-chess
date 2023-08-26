#!/bin/bash

# Install Python, pip, and PostgreSQL adapter
sudo apt -y update
sudo apt -y install python3
sudo apt -y install python3-pip
pip3 install psycopg2-binary

# Install and start Nginx
sudo apt -y install nginx
sudo service nginx start

# Navigate to your project directory
cd ~/mm-chess/chess7

# Install project dependencies
pip3 install -r requirements.txt

# Clear existing Nginx configurations
sudo rm -f /etc/nginx/sites-enabled/*
sudo rm -f /etc/nginx/sites-available/*

# Copy Nginx site configuration to available sites
sudo cp ~/mm-chess/mm-chess.conf /etc/nginx/sites-available/

# Create a symbolic link to enable the site
sudo ln -s /etc/nginx/sites-available/mm-chess.conf /etc/nginx/sites-enabled/

# Test and reload Nginx configuration
sudo nginx -t
sudo service nginx restart

# Run gunicorn to serve the Django application
gunicorn --bind localhost:8000 chess5.wsgi:application &
