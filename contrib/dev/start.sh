#!/bin/bash


python /app/check_conn.py --service-name db --port 5432  --ip db

poetry run python /app/manage.py makemigrations
poetry run python /app/manage.py migrate --fake-initial
python /app/manage.py collectstatic --noinput
cd /app

poetry run gunicorn -b 0.0.0.0:8000  project.wsgi


