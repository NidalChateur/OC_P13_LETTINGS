[![Python](https://raw.githubusercontent.com/NidalChateur/badges/779ce02cc0ce5bdc16ca2fe297b1229d4e5068d3/svg/python.svg)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/django-5.0.1-blue.svg?logo=django)](https://www.djangoproject.com/)
[![Poetry](https://img.shields.io/badge/poetry-1.7.1-blue.svg?logo=Poetry)](https://python-poetry.org/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Flake8](https://img.shields.io/badge/linting-flake8-yellowgreen.svg?logo=python)](https://github.com/pycqa/flake8)
[![Pylint](https://img.shields.io/badge/linting-pylint-yellowgreen.svg?logo=python)](https://github.com/pylint-dev/pylint)
[![codecov](https://codecov.io/gh/NidalChateur/OC_P13_LETTINGS/graph/badge.svg?token=6HKLEQ2T9G)](https://codecov.io/gh/NidalChateur/OC_P13_LETTINGS)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/c8e5ed7215db4f5894baebb12f41f867)](https://app.codacy.com/gh/NidalChateur/OC_P13_LETTINGS/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/NidalChateur/OC_P13_LETTINGS/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/NidalChateur/OC_P13_LETTINGS/tree/main)
[![Documentation Status](https://readthedocs.org/projects/oc-p13-lettings/badge/?version=latest)](https://oc-p13-lettings.readthedocs.io/en/latest/?badge=latest)
[![Docker](https://img.shields.io/badge/dockerhub-images-important.svg?logo=docker)](https://hub.docker.com/r/nidalchateur/oc_lettings_site)

# CI/CD Pipeline : OC LETTINGS SITE

<p align="center">
  <img src="./home/static/assets/img/icon.png" alt="icon">
</p>

## 1. Read the docs

<a href="https://oc-p13-lettings.readthedocs.io/en/latest/index.html">Documentation</a>

## 2. Install and run with poetry

####  0. Informations

- Locally, no environment variable is required.

- oc_letting_site.settings.local.py is active to avoid Sentry logs and environment variables.

####  1. Install dependencies

- `python -m pip install pip==23.3.2`
- `pip install poetry==1.7.1`
- `poetry install`

####  2. Run

- `poetry run python manage.py migrate`
- `poetry run python manage.py runserver`

## 3. Run the app with Docker Compose

####  1. Installer Docker 

- https://docs.docker.com/get-docker/ 

#### 2. Open shell and check Docker Compose version

- `docker compose version`

####  3. Run

- `docker compose up`

#### 4. Stop and clean system

- `docker compose down`

## CircleCI : pipeline config

####  Informations

- oc_letting_site.settings.local.py is active to avoid Sentry logs.

- Set these environment variables on the project settings :
    1. RENDER_DEPLOY_HOOK_URL (acquired from Render Web Service)
    2. DOCKERHUB_USERNAME (acquired from Docker hub)
    3. DOCKERHUB_PASSWORD (acquired from Docker hub)


## Render : web service config

####  Informations

- oc_letting_site.settings.production.py is active !

- Set these environment variables on the Web Service :
    1. SECRET_KEY (generated on Render Web Service),
    2. PYTHON_VERSION=3.10.11
    3. DJANGO_SETTINGS_MODULE=oc_lettings_site.settings.production
    4. DATABASE_URL (acquired from Render PostgreSQL)
    5. SENTRY_DSN (acquired from Sentry)
    6. ADMIN_PASSWORD (chosen on Render Web Service)