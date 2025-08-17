# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django web application that demonstrates user authentication using django-allauth and includes a todo task management system. The project is written primarily in Japanese and serves as a learning example for Django authentication patterns.

## Development Setup

### Initial Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Database setup (delete existing db.sqlite3 if starting fresh)
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Running the Application
```bash
# Development server
python manage.py runserver

# Server runs on http://localhost:8000 by default
# Admin interface: http://localhost:8000/admin/
```

### Testing
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test accounts
python manage.py test todo_task

# Run specific test files
python manage.py test todo_task.tests.test_models
python manage.py test todo_task.tests.test_views
python manage.py test todo_task.tests.test_forms
```

### Database Options
- **Default**: SQLite3 (development)
- **PostgreSQL**: Configuration available in settings.py (commented out)
- **MySQL**: Docker compose files available in `docker_compose/` directory

## Architecture

### Django Project Structure
- **django_web_allauth/**: Main Django project directory with settings and root URL configuration
- **accounts/**: Custom user authentication app extending django-allauth
- **todo_task/**: Task management CRUD application with user association

### Authentication System
- Uses django-allauth for comprehensive authentication
- Email-based login (configured in settings)
- Custom user model: `accounts.models.CustomUser`
- Mandatory email verification for new registrations
- Rate limiting configured for login attempts and signups

### Key Models
- **CustomUser**: Extended user model with custom manager
- **Task**: Todo task model with user relationship, supports title, description, due_date, and completion status

### Template Structure
- **Base templates**: Located in `templates/` directory
- **App-specific templates**: 
  - `templates/accounts/` for authentication views
  - `templates/todo_task/` for task management views
- **Bootstrap styling**: Used throughout the application

### URL Configuration
- Root URL serves home template
- `/accounts/` - All django-allauth authentication URLs
- `/todo_task/` - Task management functionality
- `/admin/` - Django admin interface

## Database Configuration

### Settings Module
The Django settings module is `django_web_allauth.settings`.

### Default Database
SQLite3 is used by default with the database file `db.sqlite3` in the project root.

### Alternative Databases
PostgreSQL and MySQL configurations are available but commented out in settings.py. Docker compose files are provided in `docker_compose/` for easy database setup.

## Security Notes
- DEBUG is set to True (development only)
- Secret key is hardcoded (should be environment variable in production)
- Console email backend used in DEBUG mode
- ALLOWED_HOSTS set to accept all hosts (development only)

## Development Notes
- Language: Japanese (LANGUAGE_CODE = 'ja')
- Timezone: Asia/Tokyo
- Logging configured to output to both console and file (`debug.log`)
- django-debug-toolbar included for development
- Unit tests available in both apps under `tests/` directories