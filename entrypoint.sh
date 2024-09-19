#!/bin/sh

# Apply database migrations
python manage.py migrate

# Collect static files (optional)
# python manage.py collectstatic --noinput

# Run the Django server
exec "$@"