@echo off

:: Check if virtualenv exists, and create it if necessary
IF NOT EXIST "venv" (
    echo Creating a virtual environment...
    python -m venv venv
)

:: Activate the virtual environment
echo Activating the virtual environment...
call venv\Scripts\activate.bat

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

:: Create migrations for any model changes
echo Creating migrations for model changes...
python manage.py makemigrations

:: Apply migrations (sets up the SQLite database)
echo Applying migrations...
python manage.py migrate

:: Create a superuser (optional, uncomment if needed)
:: python manage.py createsuperuser

:: Run the Django tests
echo Running the Django tests...
python manage.py test

:: Deactivate the virtual environment
deactivate

:: Pause so you can see the results
pause
