
FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip uninstall django
RUN pip install -r requirements.txt


# FROM python:3.8-alpine
# MAINTAINER vivek app development
# ENV PYTHONBUFFERED 1
# COPY ./requirements.txt /requirements.txt
# RUN pip3 install -r  /requirements.txt

# RUN mkdir /corerecipe
# WORKDIR /corerecipe
# COPY ./corerecipe /corerecipe
# RUN adduser -D user
# USER user

