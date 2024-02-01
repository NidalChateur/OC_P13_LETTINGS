1. Getting started
==================

1. Run and Stop
---------------

   **1. Clone the repository and run with docker-compose**

      .. code-block:: console

         $ git clone https://github.com/NidalChateur/OC_P13_LETTINGS
         $ cd OC_P13_LETTINGS
         $ docker compose up


   **2. Stop**

      .. code-block:: console

         $ docker compose down

2. Update the app
-----------------

   **Modify home/templates/index.html**

      Change "Welcome to Holiday Homes" to "Bienvenidos"

3. Tests
--------

   **1. Install dependencies**

   .. code-block:: console

      $ pip install poetry
      $ poetry install

   **2. pytest cov**

   .. code-block:: console

      $ poetry run pytest --cov=. --cov-fail-under=80

   **3. flake8**

   .. code-block:: console

      $ poetry run flake8


4. Setup CI/CD
--------------

   **1. Sign up to Docker then build and push to registery**

      https://hub.docker.com/

      .. code-block:: console

         $ docker build -t $DOCKERHUB_USERNAME/oc_lettings_site .
         $ docker push $DOCKERHUB_USERNAME/oc_lettings_site

   **2. Sign up to Render then create your PostgreSQL and Web Service**

      https://render.com/, you could follow this `Render tutorial <https://github.com/NidalChateur/OC_P13_LETTINGS/mission/Déploiement avec Render.pdf>`_

      then define environment variables on the Web Service:
         - **SECRET_KEY** (generated on Render Web Service),
         - **PYTHON_VERSION=3.10.11**
         - **DJANGO_SETTINGS_MODULE=oc_lettings_site.settings.production**
         - **DATABASE_URL** (acquired from Render PostgreSQL)
         - **SENTRY_DSN** (acquired from Sentry)
         - **ADMIN_PASSWORD** (chosen on Render Web Service)
      
   **3. Sign up to CircleCI and setup the project pipeline** 

      https://circleci.com/ you could follow this `Circleci tutorial <https://circleci.com/blog/continuous-integration-for-django-projects/>`_

      then define environment variables on the Web Service:
        - **DOCKERHUB_USERNAME** (acquired from Docker hub)
        - **DOCKERHUB_PASSWORD** (acquired from Docker hub)
        - **RENDER_DEPLOY_HOOK_URL** (acquired from Render Web Service)

5. Run CI/CD
-------------

    **Commit and push to github**

      .. code-block:: console

            (env) $ git add .
            (env) $ git commit -m "run ci"
            (env) $ git push