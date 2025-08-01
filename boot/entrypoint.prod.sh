#!/usr/bin/env bash

export PYTHONPATH=/app/src

python manage.py collectstatic --noinput
python manage.py migrate --noinput

# Start the Gunicorn server
# Use environment variables to set the host and port
# Default values are provided if not set
RUNTIME_PORT=${RUNTIME_PORT:-8000}
RUNTIME_HOST=${RUNTIME_HOST:-0.0.0.0}

python -m gunicorn --bind $RUNTIME_HOST:$RUNTIME_PORT --workers 3 src.rest_weather.wsgi:application
