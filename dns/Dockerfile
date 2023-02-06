FROM alpine:latest
RUN apk add bind openrc
RUN rc-update -u named
RUN mkdir -p /home/app/staticfiles