#!/usr/bin/env bash
# exit on error
set -o errexit

# Upgrade pip to the latest version
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Test computer vision libraries
echo "Testing computer vision libraries..."
python test_cv.py

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate