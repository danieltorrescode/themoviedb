#!/bin/sh

set -e

python manage.py test

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module app.wsgi
