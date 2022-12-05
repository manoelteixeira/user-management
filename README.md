# Flask User Management

## Content
- [Overview](#overview)
- [Features](#features)
- [Setup Instruction](#setup-instruction)
    - [Using venv](#using-venv)
    - [Using Pipenv](#using-pipenv)
- [Running the Flask Application](#running-the-flask-application)
    - [Setup up Flask environment variables](#setup-flask-environment-variables)
    - [Database Initialization](#database-initialization)
- [Key Python Modules Used](#key-python-modules-used)
- [Testing](#testing)
- [To Do](#to-do)

***

## Overview

This Flask application implements a basic user management system that can be used as a starting point for more compleplex Flask applications.

## Features
- Register
- Loging
- Logout
- Change Password

## Setup Instructions
### Using venv:
1. Clone repository:
    ```shell
    $ git clone https://github.com/manoelteixeira/user-management.git
    ```
2. Create a new virtual environment:
    ```shell
    $ cd user-management
    $ python3 -m venv venv
    ```
3. Activate virtual environment:
    ```shell
    $ source venv/bon/activate
    ```
4. Install required python packages (specified in requirements.txt):
    ```shell
    (venv) $ pip install -r requirements.txt
    ```

### Using Pipenv:
1. Install Pipenv:
    ```shell
    $ pip install pipenv
    ```
2. Clone repository:
    ```shell
    $ git clone https://github.com/manoelteixeira/user-management.git
    ```
3. Create a new virtual environment and install required python packages:
    ```shell
    $ pipenv install
    ```
## Running the Flask Application
Activate virtual environment:
- venv:
    ```shell
    $ source venv/bon/activate
    ```
- pipenv:
```shell
$ pipenv shell
```

### Setup Flask environment variables:
- Manual setup (need to be executed every time the virtual environment is activated):
    ```shell
    $ export APPLICATION_SETTINGS=../app_settings.cfg
    $ export FLASK_APP=app.py
    $ export FLASK_DEBUG=true
    ```
- Automatic setup:
    1. Install python-dotenv:
        ```shell
        $ pip install python_dotenv
        ```
    2. Create a `.env` file and add:
        ```
        APPLICATION_SETTINGS=../app_settings.cfg
        FLASK_APP=app.py
        FLASK_DEBUG=true 
        ```
### Database Initialization:
- Using Flask command line command:
    ```shell
    flask init-db
    ```

- Using `Flask shell`:
    ```shell
    flask shell
    ```
    ```python
    from app import db
    import app.models

    db.drop_all() # if database file already exists
    db.create_all() # create all tables
    exit()
    ```
**Running the application:**

After activating the virtual environment, setting up the Flask virtual environments and initializing the database (if needed):
```shell
(venv) $ flask run
```

## Key Python Modules Used
- [Flask](https://flask.palletsprojects.com)
- [Flask-Login](https://flask-login.readthedocs.io)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com)
- [Flask-WTF](https://flask-wtf.readthedocs.io)

## Testing
1. Activate virtual environment
    ```shell
     $ source venv/bon/activate
    ```
    or 
    ```
    $ pipenv shell
    ```
2. Install pytest package:
    ```shell
    $ pip install --dev pytest
    ```
    or 
    ```
    $ pipenv install --dev
    ```
3. Running tests:
    ```shell
    $ python -m pytest -v
    ```
***
# To Do
- [ ] Email confirmation
- [ ] Password recovery 
- [ ] Improve UX and UI 