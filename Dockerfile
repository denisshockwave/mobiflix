FROM python:3.6.5

MAINTAINER "Mike Mutoro <mikemutoro@gmail.com>"

LABEL application="mobiflix-backend"

# Prevent dpkg errors
ENV TERM=xterm-256color
ENV PYTHONUNBUFFERED 1

COPY . /mobiflix
WORKDIR /mobiflix

# Install current stable version of pip
RUN pip install pip
CMD ["/bin/bash", "-c", "python3 -m venv env"]
CMD ["/bin/bash", "-c", "source .env"]
RUN pip install -r requirements.txt


CMD ["/bin/bash", "-c", "python manage.py makemigrations && python manage.py migrate"]

