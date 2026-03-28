# Django Task Manager

A full-stack task management web app built with Django. Add tasks, mark them complete, and delete them with persistent data in a database.

<p align="center">
  <img src="screenshots.png" width="700"/>
</p>

## What it does

- Add tasks
- Mark tasks as complete
- Delete tasks
- Data persists in SQLite database

## Tech Stack

- Python 3
- Django 6 — web framework
- SQLite — database
- Jinja2 — templating

## Running Locally
```bash
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

## Key Concepts

- Django models and migrations
- Django ORM — `objects.create()`, `objects.all()`, `objects.get()`
- CSRF protection on forms
- URL routing and views
- Jinja2 template rendering

## Author

**Omobolanle Sadela**  
[GitHub](https://github.com/bolanlesadela) · [LinkedIn](https://www.linkedin.com/in/omobolanle-sadela-7a486a1b4/)
