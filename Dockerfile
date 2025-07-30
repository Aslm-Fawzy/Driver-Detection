# Use official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port your Flask app runs on
EXPOSE 8890

# Default command to run the Flask app with Gunicorn
CMD ["gunicorn", "--config", "API/gunicorn_config.py", "API.app:app"]
