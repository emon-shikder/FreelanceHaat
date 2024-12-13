#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations (if necessary)
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput