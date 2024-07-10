This Django-based web application is designed to manage campus security employees. It leverages HTML, CSS, JavaScript, and Bootstrap for the front-end to ensure a responsive and user-friendly interface.

# Table of Contents
Features
Technologies Used
Installation
Usage
Screenshots
Contributing
License

# Features
Employee Registration and Management
Duty Roster Management
Attendance Tracking
Incident Reporting
User Authentication and Authorization
Responsive Design

# Technologies Used
Backend
Django
SQLite 
Frontend
HTML
CSS
JavaScript
Bootstrap

# Installation
Prerequisites
Python 3.11.5
pip (Python package installer)
virtualenv 

# Steps
Clone the repository:

git clone https://github.com/your-username/campus-security-management.git
cd CampusSecurity

Create and activate a virtual environment:

python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the required packages:

pip install -r requirements.txt

Apply the migrations:
python manage.py migrate

Create a superuser:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/ to access the application.

Usage
Admin Panel
Access the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials.




