Local install with pip and run
==============================

Install and run
---------------

    **1. Clone the repository**

        .. code-block:: console

            $ git clone https://github.com/NidalChateur/OC_P13_LETTINGS
            $ cd OC_P13_LETTINGS
    
    **2. Set up a virtual environment**
        
        .. code-block:: console

            $ python -m venv env 
    
    **3. Activate virtual environment**

        - Windows
            .. code-block:: console

                $ env/scripts/activate

        - Unix/MacOS
            .. code-block:: console

                $ source env/bin/activate
    
    **4. Install dependencies**

        .. code-block:: console

            (env) $ python -m pip install pip==23.3.2
            (env) $ pip install -r requirements/local_freeze.txt

    **5. Run**

        .. code-block:: console

            (env) $ python manage.py runserver
        
        When the server is running, the application can be accessed from the URL [http://127.0.0.1:8000/].

        Steps 1, 2, and 4 are only required for the initial installation. For subsequent launches of the application server, simply execute steps 3 and 5 from the project's root directory.
    
Flake8 linting
--------------

    Flake8 is commonly used to check adherence to Python PEP 8 style conventions in code. To do this, navigate to the project's root directory and run the following commands in the terminal:

    .. code-block:: console

        (env) $ flake8

    An error report in HTML format will then be available in the 'flake8_html_report' directory.

Pytest coverage
---------------

    The test coverage checks the percentage of lines covered by tests.

    To achieve this, navigate to the project's root directory and run the following commands in the terminal:

    .. code-block:: console

        (env) $ pytest --cov=. --cov-report html

    Once the script is complete, you will find that a new folder called 'htmlcov' has been created where you executed the command.

    Open the "htmlcov/index.html" file.