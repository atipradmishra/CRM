# CRM Project

A simple Customer Relationship Management (CRM) system built using Django. This project allows users to manage customer data, track sales, and provide a clear interface for handling customer interactions.

## Features

- **Customer Management**: Create, view, update, and delete customer information.
- **Sales Tracking**: Log and view sales activities linked to individual customers.
- **Authentication**: Secure login for different user roles (e.g., Admin, Sales Team).
- **Search and Filter**: Easily search and filter customer records based on name, email, or sales data.
- **Responsive Design**: User-friendly interface, responsive across devices.
- **Dashboard**: Overview of recent activities, customer data, and sales metrics.
- **Export Data**: Ability to export customer data to CSV.

## Tech Stack

- **Backend**: Django 4.x (Python 3.8+)
- **Database**: PostgreSQL or SQLite
- **Frontend**: HTML5, CSS3, JavaScript (optional: Bootstrap)
- **Authentication**: Django's built-in authentication system
- **Others**: Django Rest Framework (optional, for API development)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/crm-django.git
    cd crm-django
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

    Access the app at `http://127.0.0.1:8000`.

## Usage

1. Log in using the superuser credentials or create a new user account.
2. Use the navigation bar to access customers, sales, and other features.
3. Track customer interactions and sales through the dashboard.

## Project Structure

```bash
crm/
│
├── agents/                 # Main application folder
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates for the frontend
│   ├── static/             # Static files (CSS, JS, images)
│   ├── views.py            # Business logic and rendering views
│   ├── models.py           # Database models for customers, sales, etc.
│   └── urls.py             # URL routing for the app
│   └── admin.py            # Admin Page for the app
│   └── apps.py
│   └── forms.py            # Forms for the app
│   └── resources.py        # Decoratater for authentication
│
├── crm/                    # Main Django project folder
│   ├── asgi.py  
│   ├── settings.py         # Configuration and settings
│   ├── wsgi.py  
│   └── urls.py             # Main URL routing
│
├── customers/              # Main application folder
│   ├── migrations/         # Database migrations
│   ├── views.py            # Business logic and rendering views
│   ├── models.py           # Database models for customers, sales, etc.
│   └── urls.py             # URL routing for the app
│   └── admin.py            # Admin Page for the app
│   └── apps.py
│   └── forms.py            # Forms for the app
│
├── leads/                  # Main application folder
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates for the frontend
│   ├── static/             # Static files (CSS, JS, images)
│   ├── views.py            # Business logic and rendering views
│   ├── models.py           # Database models for customers, sales, etc.
│   └── urls.py             # URL routing for the app
│   └── admin.py            # Admin Page for the app
│   └── apps.py
│   └── forms.py            # Forms for the app
│   └── resources.py        # Decoratater for authentication
│
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates for the frontend    
├── manage.py               # Django's command-line utility
└── requirements.txt        # Python dependencies
