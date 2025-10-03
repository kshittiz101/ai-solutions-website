#!/bin/bash

# Build script for Vercel deployment
echo "Starting build process..."

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Run migrations (optional - comment out for production)
# echo "Running database migrations..."
# python manage.py migrate --noinput

# Load demo data (optional - only for first deployment)
# echo "Loading demo data..."
# python manage.py loaddata demo_data.json

echo "Build completed successfully!"

