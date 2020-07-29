FROM ubuntu:20.04

FROM python:3.8

RUN apt-get update && apt-get install -y software-properties-common

RUN add-apt-repository ppa:ubuntugis/ppa

RUN apt-get install -y binutils libproj-dev gdal-bin libsqlite3-mod-spatialite

RUN mkdir /code

COPY . /code/

COPY requirements.txt /code

COPY .env.example /code/.env

WORKDIR /code

RUN pip install -r requirements.txt