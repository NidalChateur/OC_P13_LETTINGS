Context
=======

1. Specifications
-----------------

- `App specifications <https://github.com/NidalChateur/OC_P13_LETTINGS/mission/cahier des charges.pdf>`_ 
- `Doc specifications <https://github.com/NidalChateur/OC_P13_LETTINGS/mission/read the docs.pdf>`_ 

2. Project description
----------------------

   Overhaul of the modular architecture in the `GitHub repository <https://github.com/NidalChateur/OC_P13_LETTINGS>`_  

      1. Addressing various technical debts in the project  

      2. `Dockerize <https://hub.docker.com/repository/docker/nidalchateur/oc_lettings_site/general>`_  

      3. Implementation of a CI/CD pipeline using `CircleCI <https://app.circleci.com/pipelines/github/NidalChateur/OC_P13_LETTINGS>`_ and deployment on `Render <https://render.com/>`_  

      4. Monitoring the application and tracking errors through `Sentry <https://sentry.io/>`_  

      5. Creation of the technical documentation for the application using `Read The Docs <https://about.readthedocs.com/>`_ and `Sphinx <https://github.com/sphinx-doc/sphinx>`_  


3. System Configuration
-----------------------

- Windows 11
- Visual Studio Code 1.85.2
- Powershell
- Python 3.10.11
- pip 23.3.2

4. Development packages
-----------------------

During local development, we use **oc_lettings_site/settings/local.py**
(no environment variable)

- poetry 1.7.1
- django 5.0.1
- django-maintenance-mode==0.21.1

5. Test packages
----------------

During tests, we also use **oc_lettings_site/settings/local.py**
(no environment variable for local tests)

Circleci environment variables: 
   - **DOCKERHUB_USERNAME** (acquired from Docker hub)
   - **DOCKERHUB_PASSWORD** (acquired from Docker hub)
   - **RENDER_DEPLOY_HOOK_URL** (acquired from Render)


- pytest 8.0.0
- pytest-cov 4.1.0
- pytest-django 4.8.0
- flake8 7.0.0
- flake8-html 0.4.3

6. Production packages
----------------------

During production, we use **oc_lettings_site/settings/production.py**

Render environment variables: 
   - **SECRET_KEY** (generated on Render),
   - **PYTHON_VERSION=3.10.11**
   - **DJANGO_SETTINGS_MODULE=oc_lettings_site.settings.production**
   - **DATABASE_URL** (acquired from Render)
   - **SENTRY_DSN** (acquired from Sentry)
   - **ADMIN_PASSWORD** (chosen on Render)

- gunicorn 21.2.0
- psycopg2-binary 2.9.9
- whitenoise[brotli] 6.6.0
- sentry-sdk[django] 1.40.0
- dj-database-url 2.1.0

7. Database models
------------------

.. py:class:: class Address(models.Model):
   - number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
   - street = models.CharField(max_length=64)
   - city = models.CharField(max_length=64)
   - state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
   - zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
   - country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])


.. py:class:: class Letting(models.Model):
   - title = models.CharField(max_length=256)
   - address = models.OneToOneField(Address, on_delete=models.CASCADE)


.. py:class:: class Profile(models.Model):
   - user = models.OneToOneField(User, on_delete=models.CASCADE)
   - favorite_city = models.CharField(max_length=64, blank=True)


