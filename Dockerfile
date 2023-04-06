FROM python:3.9.0-alpine

ENV PYTHONUNBUFFERED 1

COPY /src/requirements.txt /requirements.txt
RUN apk add --upgrade --no-cache build-base linux-headers && \
    pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    apk add --update nano

RUN mkdir -p /app/logs

COPY /src /app
WORKDIR /app

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8002", "portfolio.wsgi:application"]