#!/bin/bash

# Set up the virtual environment (if not already set up)
if [ ! -d "venv" ]; then
  echo "Creating a virtual environment..."
  python3 -m venv venv
fi

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Apply migrations (sets up the SQLite database)
echo "Applying migrations..."
python manage.py migrate

# Create a superuser (optional, uncomment if needed)
# echo "Creating superuser..."
# python manage.py createsuperuser

# Run the Django development server
echo "Running the Django server..."
python manage.py runserver
