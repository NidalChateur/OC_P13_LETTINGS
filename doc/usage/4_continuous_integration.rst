4. Continuous integration (CI)
==============================

Prerequisite
-------------

    0. At this step you could comment the job "deploy" on ./circleci/config.yml

    1. Fork the repository
    
    2. Sign up to `Docker Hub <https://hub.docker.com/>`_.

    3. Sign up to `CircleCI <https://circleci.com/>`_ 

    4. CircleCI : Setup your project pipeline by seleting your github repository, you could follow this `tutorial <https://circleci.com/blog/continuous-integration-for-django-projects/>`_.

    5. CircleCI : finaly, define your project environment variables in project settings : 
        - **DOCKERHUB_USERNAME** (acquired from Docker hub)
        - **DOCKERHUB_PASSWORD** (acquired from Docker hub)



Local controls > Push to github
-------------------------------

    **1. Local controls before commit and push to github**

        .. code-block:: console

            (env) $ poetry run flak8
            (env) $ poetry run pytest --cov=. --cov-fail-under=80
            (env) $ docker compose up
            (env) $ circleci config validate
            
        
        if all tests passed, you can commit !

    **3. Commit and push modifications to github**

        .. code-block:: console

            (env) $ git add .
            (env) $ git commit -m "run ci"
            (env) $ git push

    **3. Visite your project pipeline on Circleci**

        Check :
            - test ✅
            - build ✅

        if you have a fail, open circleci logs to debug then fix the bug locally. After that you could repeat 
        local controls > push to github steps.