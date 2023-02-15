FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

COPY /src/requirements.txt /requirements.txt
RUN apk add --upgrade --no-cache build-base linux-headers && \
    pip install --upgrade pip && \
    pip install -r /requirements.txt

COPY /src /app
WORKDIR /app

RUN adduser --disabled-password --no-create-home django

USER django

CMD ["uwsgi", "--socket", ":9000", "--workers", "4", "--master", "--enable-threads", "--module", "portfolio.wsgi"]