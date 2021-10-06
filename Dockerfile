FROM python:3.10.0-alpine3.14
LABEL maintainer "sksat <sksat@sksat.net>"

RUN apk add --update --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache build-base

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD entrypoint.py .
ENTRYPOINT ["/entrypoint.py"]
