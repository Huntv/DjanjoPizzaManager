# Django Pizza Manager

## Brief Overview

A web application to manage pizza orders with different user roles (e.g., PizzaOwner, PizzaChef). This project is built using Django and runs on a local SQLite database. On the cloud it runs on postgreSQL.


I chose Django as the framework for this project because Python was the preferred language, and I was already familiar with it. I initially encountered challenges with deploying and testing the .NET framework on my local machine, which led me to switch to Django. For the frontend, I opted for basic HTML as it was the most familiar to me and met the needs of the current stories without introducing unnecessary complexity.

While I began with Azure for hosting, I ran into deployment issues with my Django application, and the deployment process was slower than expected. This led me to transition to AWS, where I gained more control over the environment by connecting to a Linux server, offering better flexibility for my deployment needs.


##Links
- AWS Deployment: http://3.18.70.54/
## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.11
- pip (Python package installer)

## Manual Setup and Installation (Option 1)

To set up and run the project locally, follow these steps:

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/DjanjoPizzaManager.git
cd DjanjoPizzaManager
```

### 2. Setup Virtual Envirnoment
```
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run Server
```
python manage.py runserver

```
The development server should be deployed at http://127.0.0.1:8000/

## Automated Setup and Installation (Option 2)

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/DjanjoPizzaManager.git
cd DjanjoPizzaManager
```

### 2. Run .bat file
```
  run_django.bat
```

The development server should be deployed at http://127.0.0.1:8000/

## Run test locally

```
  run_djangotest.bat
```
## Brief Overview on Application


