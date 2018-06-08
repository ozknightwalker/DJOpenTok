#!/bin/sh

echo migrate django project
python manage.py migrate
echo collectstatic django project
python manage.py collectstatic --noinput;
echo Starting Gunicorn Server
gunicorn -w 3 -b 0.0.0.0:${WEB_SERVER_PORT} djopentok.wsgi
