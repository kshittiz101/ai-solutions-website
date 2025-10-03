#!/bin/bash

# Build script for Vercel deployment
echo "Starting build process..."

# Install pipenv if not available
echo "Installing pipenv..."
pip install pipenv

# Install dependencies using pipenv
echo "Installing Python dependencies with pipenv..."
pipenv install --deploy --ignore-pipfile

# Collect static files
echo "Collecting static files..."
pipenv run python manage.py collectstatic --noinput --clear

# Run migrations (optional - comment out for production)
# echo "Running database migrations..."
# pipenv run python manage.py migrate --noinput

# Load demo data (optional - only for first deployment)
# echo "Loading demo data..."
# pipenv run python manage.py loaddata demo_data.json

echo "Build completed successfully!"

