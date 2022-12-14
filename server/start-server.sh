#!/usr/bin/env bash
python manage.py migrate --noinput & 
gunicorn config.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 &
nginx -g "daemon off;"