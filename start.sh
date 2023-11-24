#!/bin/bash

# Start Nginx in the background
service nginx start

# Start Gunicorn for your Django application
cd /usr/src/app/chess7
gunicorn --bind localhost:8000 chess5.wsgi:application

