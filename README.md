[![Python](https://raw.githubusercontent.com/NidalChateur/badges/779ce02cc0ce5bdc16ca2fe297b1229d4e5068d3/svg/python.svg)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/django-5.0.1-blue.svg?logo=django)](https://www.djangoproject.com/)
[![Poetry](https://img.shields.io/badge/poetry-1.7.1-blue.svg?logo=Poetry)](https://python-poetry.org/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Flake8](https://img.shields.io/badge/linting-flake8-yellowgreen.svg?logo=python)](https://github.com/pycqa/flake8)
[![Pylint](https://img.shields.io/badge/linting-pylint-yellowgreen.svg?logo=python)](https://github.com/pylint-dev/pylint)
[![Codecov](https://codecov.io/gh/NidalChateur/new_test_p13/graph/badge.svg?token=0NAIURXDSL)](https://codecov.io/gh/NidalChateur/new_test_p13)
[![Codacy](https://app.codacy.com/project/badge/Grade/8c5fd6f292da4f96b65080520cf5f194)](https://app.codacy.com/gh/NidalChateur/new_test_p13/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/NidalChateur/new_test_p13/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/NidalChateur/new_test_p13/tree/main)
[![Docker](https://img.shields.io/badge/dockerhub-images-important.svg?logo=docker)](https://hub.docker.com/repository/docker/nidalchateur/oc_lettings_site/general)

#

<p align="center">
  <img src="./home/static/assets/img/icon.png" alt="icon">
</p>




## Lancer l'application avec Docker

####  1. Installer Docker si ce n'est pas déjà fait
- https://docs.docker.com/get-docker/ 

#### 2. Ouvrir un terminal et vérifier que Docker soit bien installé
- `docker --version`

####  3. Lancer l'application
- lancer l'app en premier plan
    - `docker run -p 8000:8000 nidalchateur/oc_lettings_site`

- lancer l'app en arrière plan
    - `docker run -d -p 8000:8000 nidalchateur/oc_lettings_site`

- ouvrir le shell du conteneur
    - `docker run -it nidalchateur/oc_lettings_site /bin/bash`

#### 4. Stopper l'application

1. Lister les conteneurs en cours d'execution

    - `docker ps`

2. Stopper le conteneur en cours d’exécution

    - `docker stop container_id`

4. Nettoyer le système

    - `docker system prune`

5. Supprimer l'image 

    - `docker rmi nidalchateur/oc_lettings_site`

6. Verifier que l'image a bien été supprimée

    - `docker images`


## Lancer l'application avec Docker Compose

####  1. Installer Docker si ce n'est pas déjà fait

- https://docs.docker.com/get-docker/ 

#### 2. Ouvrir un terminal et vérifier que Docker soit bien installé

- `docker compose version`

####  3. Lancer l'application
- lancer l'app en premier plan

    - `docker compose up`

#### 4. Stopper l'application

- `docker compose down`