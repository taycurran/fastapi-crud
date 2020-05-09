# pull official base image
FROM python:3.8.1-alpine

# So, we started with an Alpine-based Docker image for 
# Python 3.8.1. 

# set work directory
WORKDIR /usr/src/app

# We then set a working directory along with 
# two environment variables:

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Finally, we copied over the requirements.txt file, 
# installed some system-level dependencies, 
# updated Pip, 
# installed the requirements, 
# and copied over the FastAPI app itself.

# copy requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . /usr/src/app/