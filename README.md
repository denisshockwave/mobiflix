# Mobiflix
Local On demand streaming service


Create a virtualenv for python 3
Run install pip install -r requirements.txt

python manage.py migrate

python manage.py runserver


To read documentation  go to
http://127.0.0.1:8000/docs


VERIFY VOUCHER api

{
    "message": "Hey that voucher does not exist.",
    "state": "danger",
    "status": "POSTER"
}

{
    "message": "Your message has expired",
    "state": "danger",
    "status": "POSTER"
}

{
    "message": "Code has bee verified",
    "state": "success",
    "expiry_date": "2019-02-15 14:45:00",
    "status": "WATCH"
}

Retrieve movie after voucher has been verified
Store expiry date in a cookie and try analyze it to check expiry datetime


## Docker Container

Go to the project directory and run the following commands:

- START: `make start` to run the application
- STOP: `make stop` to stop the application and destroy the container and the image
- HELP: `make help` to view the list of available options