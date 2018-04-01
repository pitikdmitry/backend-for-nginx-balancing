FROM ubuntu:16.04

MAINTAINER Dmitry Pitik

ADD ./ /my_application

RUN apt-get update
RUN apt-get install python-pip -y

RUN pip install -r /my_application/requirements.txt

USER root
WORKDIR /my_application

CMD gunicorn --bind 0.0.0.0:8000 wsgi