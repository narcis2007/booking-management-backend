# kick-starter-python
This is a kick starter for a project that the students in ASSIST internship will be doing.

How to install the application
------------------------------

- Clone the code from git.
- Create an environment using [virtualenv](https://virtualenv.pypa.io/en/latest/) and activate it.
- Install the project dependencies with [pip](https://pip.pypa.io/en/latest/installing.html). Run this command: `pip install -r requirements.txt` while being in the folder with the `requirements.txt` file.
- Access mysql server using: `mysql -u root -p` and create the database: `CREATE DATABASE kick_start;`
- Create the following `local_settings.py` file in the same folder as `settings.py`:
```
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'kick_start',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': '',
    'PORT': ''
    }
}
DEBUG = True
```
- Run `python manage.py migrate` to create the tables.
- Run `python manage.py runserver` to actually run the application.
