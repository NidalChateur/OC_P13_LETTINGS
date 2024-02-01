5. Continuous delivery (CD)
===========================

1. Prerequisite
----------------

    0. Uncomment the "deploy" job on .circleci/config.yml

    1. Sign up to `Sentry <https://sentry.io/welcome/>`_ to get the **SENTRY_DSN**, you could follow this `tutorial <https://docs.sentry.io/platforms/python/integrations/django/>`_

    2. Sign up to `Render <https://render.com/>`_

    3. On Render firstly, create your PostgreSQL Database to get your **DATABASE_URL**, save "Internal Database URL" as **DATABASE_URL**. 

    4. On Render, now create your Web Service, you could follow this `Render tutorial <https://github.com/NidalChateur/OC_P13_LETTINGS/mission/Déploiement avec Render.pdf>`_

    5. Then define environment variables on the Render Web Service :
        - **SECRET_KEY** (generated on Render Web Service),
        - **PYTHON_VERSION=3.10.11**
        - **DJANGO_SETTINGS_MODULE=oc_lettings_site.settings.production**
        - **DATABASE_URL** (acquired from Render PostgreSQL)
        - **SENTRY_DSN** (acquired from Sentry)
        - **ADMIN_PASSWORD** (chosen on Render Web Service)
    
    6. Finaly, in your CircleCI add this environment variable in project settings :
        - **RENDER_DEPLOY_HOOK_URL** (acquired from Render Web Service)
   

2. Run continuous integration
------------------------------

    1. Make your local controls and assure all is ok.

    2. Commit and push modifications to github

    3. Visite your project pipeline on Circleci

        Check :
            - test ✅
            - build ✅
            - deploy ✅

        if you have a fail, open circleci logs to debug then fix the bug locally. After that you could repeat 
        local controls > push to github steps.

    4. Visite your Web Service on Circleci

        Check events :
            - A new deploy should start ⬆️ : "Triggered via Deploy Hook"
            - Deploy is live ✅
    
    5. If the pipeline run succeed and the deploy too, the pipeline CI/CD is now working !

    
