# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory for Django application
WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update -y \
    && apt-get install -y \
        nginx \
        python3-pip \
        gunicorn \
        python3-stripe \
        python3-django \
        python3-django-crispy-forms \
        libpq-dev \
        python3-psycopg2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./requirements.txt /usr/src/app/
RUN pip3 install --upgrade pip setuptools wheel \
    && pip3 install -r requirements.txt

# Copy project
COPY . /usr/src/app/

# Collect static files
RUN python3 chess7/manage.py collectstatic --noinput

# Copy and configure Nginx
COPY ./mm-chess.conf /etc/nginx/sites-available/
RUN sed -i "s|PWD|/usr/src/app|g" /etc/nginx/sites-available/mm-chess.conf \
    && ln -s /etc/nginx/sites-available/mm-chess.conf /etc/nginx/sites-enabled/ \
    && rm -f /etc/nginx/sites-enabled/default \
    && rm -f /etc/nginx/sites-available/default

# Expose ports for Nginx (80) and Gunicorn (8000)
EXPOSE 80 8000

# Start Gunicorn and Nginx using a shell script
COPY start.sh /usr/src/app/
RUN chmod +x /usr/src/app/start.sh
CMD ["./start.sh"]
