FROM python:3.9.7-alpine3.14
LABEL maintainer "sksat <sksat@sksat.net>"

RUN apk add --update --no-cache jpeg-dev zlib-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD entrypoint.py .
CMD ["/entrypoint.py"]
ENTRYPOINT ["python"]
