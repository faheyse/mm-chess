# ---- Build Stage ----
# Use Python 3.9 as the base image for the build stage
FROM python:3.9 AS build

# Set environment variables for Django
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=chess5.settings

# Set the working directory in the Docker container
WORKDIR /app

# Copy requirements.txt to the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# ---- Nginx Stage ----
# Use Nginx for the final stage
FROM nginx:alpine

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy static files from build stage
COPY --from=build /app/staticfiles /static

# Copy media files
COPY --from=build /app/media /media
