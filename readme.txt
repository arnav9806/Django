# MyProject

A Django 4.2 project with Django REST Framework (DRF) and JWT authentication.

## Features

- Django 4.2.28
- Django REST Framework 3.14.0
- JWT authentication using djangorestframework-simplejwt 5.3.1
- PostgreSQL / SQLite support
- Modular app structure with `core` app
- Ready for API development and frontend integration

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/arnav9806/Django.git
cd Django
go to the main project 
Create a virtual environment

python -m venv venv
Activate the virtual environment

On Windows:

.\venv\Scripts\activate
On Linux/Mac:

source venv/bin/activate
Install dependencies

pip install --upgrade pip
pip install -r requirements.txt
Run migrations

python manage.py migrate
Create a superuser (optional for admin access)

python manage.py createsuperuser
Start the development server

python manage.py runserver
Visit http://127.0.0.1:8000/ to check your project.

Project Structure
myproject/
│
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── core/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    └── ...