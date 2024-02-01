#!/usr/bin/env bash
# exit on error
set -o errexit

poetry run python manage.py collectstatic --no-input
poetry run python manage.py makemigrations
poetry run python manage.py migrate

poetry run python manage.py shell <<EOF
from django.contrib.auth.models import User
admin = User.objects.get(username="admin")
admin.set_password("$ADMIN_PASSWORD")
admin.save()
EOF

poetry run gunicorn oc_lettings_site.wsgi:application

# to run it set on Dockerfile :
# RUN chmod a+x start_render.sh