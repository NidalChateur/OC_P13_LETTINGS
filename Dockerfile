# get Python 3.10 without shell
# FROM python:3.10-alpine

# get Python 3.10 with shell
FROM python:3.10-slim

ENV PYTHONUNBUFFERED  1 \
    PYTHONDONTWRITEBYTECODE 1 

WORKDIR /app

RUN python -m pip install pip==23.3.2 \
    && pip install poetry==1.7.1 \
    && touch README.md

COPY pyproject.toml poetry.lock ./

RUN poetry install --without dev

COPY .. .

RUN chmod a+x start_render.sh

CMD poetry run python manage.py makemigrations\
    && poetry run python manage.py migrate \
    && poetry run python manage.py runserver 0.0.0.0:8000


