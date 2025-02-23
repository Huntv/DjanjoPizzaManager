# Django Pizza Manager

## Brief Overview

A web application to manage pizza orders with different user roles (e.g., PizzaOwner, PizzaChef). This project is built using Django and runs on a local SQLite database. On the cloud it runs on postgreSQL.


I chose Django as the framework for this project because Python was the preferred language, and I was already familiar with it. I had also encountered difficulties testing the .NET framework locally, which made Django a more suitable option. For the frontend, I used basic HTML since it was the most familiar to me and met the needs of the project without introducing unnecessary complexity.

Initially, I hosted the application on Azure, but I faced deployment issues and experienced slow deployment times. As a result, I switched to AWS, which provided more control over the environment by allowing me to connect to a Linux server. This transition gave me the flexibility I needed to manage the application more effectively.

For local development, I used SQLite as the database due to its simplicity and ease of installation. However, for deployment on AWS, I switched to PostgreSQL to ensure better compatibility with the cloud environment and to leverage its more robust features for production use.


## Links
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

