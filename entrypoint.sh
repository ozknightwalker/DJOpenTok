#!/bin/sh

echo Starting Gunicorn Server
gunicorn -w 3 -b 0.0.0.0:${WEB_SERVER_PORT} djopentok.wsgi
