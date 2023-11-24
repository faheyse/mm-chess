# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install Nginx
RUN apt-get update && apt-get install -y nginx && apt-get clean
RUN apt install -y python3-pip
RUN apt install -y gunicorn
RUN apt install -y python3-stripe
RUN apt -y install python3-django
RUN apt -y install python3-django-crispy-forms
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory for Django application
WORKDIR /usr/src/app

# Install Python dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install --upgrade pip setuptools wheel
RUN apt-get install -y libpq-dev
RUN apt-get install -y python3-psycopg2
RUN pip3 install -r requirements.txt

# Copy project
COPY . /usr/src/app/

# Collect static files
RUN python3 chess7/manage.py collectstatic --noinput

# Copy Nginx configuration file
COPY ./mm-chess.conf /etc/nginx/sites-available/
RUN sed -i "s|PWD|/usr/src/app|g" /etc/nginx/sites-available/mm-chess.conf
RUN ln -s /etc/nginx/sites-available/mm-chess.conf /etc/nginx/sites-enabled/
RUN rm /etc/nginx/sites-enabled/default
RUN rm /etc/nginx/sites-available/default
# Expose ports for Nginx (80) and Gunicorn (8000)
EXPOSE 80 8000

# Start Gunicorn and Nginx using a shell script
COPY start.sh /usr/src/app/
RUN chmod +x /usr/src/app/start.sh
CMD ["./start.sh"]

