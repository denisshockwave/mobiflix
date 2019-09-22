FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /srv/app

WORKDIR /srv/app

ADD requirements.txt /srv/app/
RUN pip install -r requirements.txt

ADD . /srv/app

