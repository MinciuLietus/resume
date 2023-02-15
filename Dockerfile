FROM python:3.9.0-alpine

ENV PYTHONUNBUFFERED 1

COPY /src/requirements.txt /requirements.txt
RUN apk add --upgrade --no-cache build-base linux-headers && \
    pip install --upgrade pip && \

COPY /src /app
WORKDIR /app

RUN pip install -r /requirements.txt
RUN python manage.py collectstatic --noinput

CMD ["uwsgi", "--socket", ":9000", "--workers", "4", "--master", "--enable-threads", "--module", "portfolio.wsgi"]