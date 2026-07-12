# Use official Python image
FROM python:3.12-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Print logs immediately
ENV PYTHONUNBUFFERED=1

# Working directory inside container
WORKDIR /app

# Copy dependency file
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app/ .

RUN adduser --disabled-password appuser

USER appuser

# Expose application port
EXPOSE 8000

# Start application
CMD ["gunicorn","--bind","0.0.0.0:8000","app:app"]
