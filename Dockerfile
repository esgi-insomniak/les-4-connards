# syntax=docker/dockerfile:1
FROM python:3.10-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /var/www
COPY requirements.txt /var/www/
RUN apt-get update
RUN alias python=python3 && pip3 install -r requirements.txt
COPY . /var/www/
# migrate db
#RUN python manage.py makemigrations
#RUN python manage.py migrate
EXPOSE 8000