# Pull base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY src/ /app/src/

# Set PYTHONPATH to include src so we can run manage.py easily
ENV PYTHONPATH "${PYTHONPATH}:/app/src"

# Run gunicorn
CMD ["gunicorn", "--chdir", "src", "curso_django.wsgi:application", "--bind", "0.0.0.0:8000"]
