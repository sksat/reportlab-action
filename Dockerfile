FROM python:3.10.4-alpine3.14
LABEL maintainer "sksat <sksat@sksat.net>"

RUN apk add --update --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache build-base

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install

ADD entrypoint.py .
ENTRYPOINT ["/entrypoint.py"]
