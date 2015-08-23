# Booking Management
This is the back end source code for the "Booking Banagement" android app made at Assist Software Summer Internship 2015

Description:
This app lets the user make and easy and fast booking at health centers near him.
Steps:
-choose a clinic from google maps
-fill in your personal data
-give us 3 dates when you are free
-write a short description of what bothers you

As soon as possible someone will contact you and settle the final date of the appointment and confirm your booking.
You can check the status of your booking anytime using the unique code received by email.

There are 3 statuses: waitting, confirmed and finalized. After the booking is made or the status of their booking is changed the user is informed with an email containing useful information.


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
