# Use Python 3.9 as the base image
FROM python:3.9

# Set environment variables for Django
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=chess7.settings

# Set the working directory in the Docker container
WORKDIR /app

# Copy requirements.txt to the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run Gunicorn for production
CMD ["gunicorn", "chess7.wsgi:application", "--bind", "0.0.0.0:80"]
