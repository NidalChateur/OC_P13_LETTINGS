Run locally the application with Docker
=======================================

1. Run
-------

    **1. Install Docker Desktop**

        https://docs.docker.com/get-docker/

        .. code-block:: console

            $ docker --version
            Docker version 24.0.7
    
    **2. Run**
        
        Run with diplayed logs

        .. code-block:: console

            $ docker run -p 8000:8000 nidalchateur/oc_lettings_site
        
        Run with hidden logs
        
        .. code-block:: console

            $ docker run -d -p 8000:8000 nidalchateur/oc_lettings_site

        When the server is running, the application can be accessed from the URL [http://127.0.0.1:8000/].

        Open Shell

        .. code-block:: console

            $ docker run -it nidalchateur/oc_lettings_site /bin/bash


2. Stop
--------

    **1. Stop and clean system**

        1. List containers

        .. code-block:: console

            $ docker ps

        2. Stop the container

        .. code-block:: console

            $ docker stop container_id

        3. Clean system

        .. code-block:: console

            $ docker system prune
        
        4. Remove image

        .. code-block:: console

            $ docker rmi nidalchateur/oc_lettings_site
    
        5. List images to check the deletion 

        .. code-block:: console

            $ docker images