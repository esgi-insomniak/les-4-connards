# syntax=docker/dockerfile:1
FROM python:3.10-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /var/www
COPY requirements.txt /var/www/
RUN alias python=python3 && pip3 install -r requirements.txt
RUN apt-get update \
    && apt-get install curl -y \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g yarn \
    && yarn install
COPY . /var/www/
EXPOSE 8000