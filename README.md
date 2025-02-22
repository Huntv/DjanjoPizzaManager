# Django Pizza Manager

A web application to manage pizza orders with different user roles (e.g., PizzaOwner, PizzaChef). This project is built using Django and runs on a local SQLite database.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Setup and Installation

To set up and run the project locally, follow these steps:

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/DjanjoPizzaManager.git
cd DjanjoPizzaManager

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
python manage.py runserver
