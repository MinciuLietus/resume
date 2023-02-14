#!/bin/sh
set -e

cd /home/bitnami/app/resume
/usr/local/bin/docker-compose -f docker-compose.deploy.yml run --rm certbot certbot renew