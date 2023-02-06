FROM python:3.9.0-alpine
COPY . ./app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install requirements
RUN pip install pip --upgrade pip
COPY ./requirements.txt ./app
RUN pip install -r requirements.txt