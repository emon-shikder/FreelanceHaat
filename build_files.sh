#!/bin/bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations (if necessary)
python manage.py migrate

# Collect static files
python manage.py collectstatic