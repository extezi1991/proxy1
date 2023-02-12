FROM python:3.8.3-alpine
# set work directory
WORKDIR /usr/src/identist
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
COPY . .
RUN pip install --upgrade pip

RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev && \
    pip install --no-cache-dir -r reqirements.txt