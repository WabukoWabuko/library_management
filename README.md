# Library Management Web Application

A web app built for a job application test, using Django, SQLite3(locally and MySQL for production), ReactJS, and Bootstrap.

## Features
- **Books**: Add, list, and search books by name/author.
- **Members**: Add and list members with debt tracking.
- **Transactions**: Issue and return books, with a KES 10/day fee and KES 500 debt limit.

## Setup
1. **Backend (Django)**:
```bash
   cd library_management
   python -m venv venv
   source venv/bin/activate  # Mac/Linux: or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   cd library_project
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
```
2. **Frontend (React):**
```bash
    cd frontend
    npm install
    npm start
```

## Usage
- Visit `http://localhost:3000/` for the frontend.
- Admin panel: `http://127.0.0.1:8000/admin/`.
- API endpoints: `/api/books/`, `/api/members/`, `/api/issue/`, `/api/return/`, `/api/search/`.

## Screenshots

- Books Page:
- Members Page:
- Transactions Page:

## Notes
Built with Django REST Framework, React Router, and Axios.
Proxy in `frontend/package.json` connects to Django.
Tests in `library_app/tests.py`.

