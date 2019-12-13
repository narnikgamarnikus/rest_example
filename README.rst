REST Example
============

REST Example

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ make superuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ make mypy

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ make coverage && open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ make test


Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog


Development
----------

The following details how to deploy this application.

::

  $ make build && make migrations && make up

Deployment
----------

The following details how to deploy this application.

::

  $ export ENVIRONMENT=production
  $ make start


API usage
----------

Registration

::

  $ curl -X POST -H "Content-Type: application/json" http://localhost:8000/api/v1/auth/registration/ -d '{"username": "testusername", "email": "test@email.com", "password1": "testpassword", "password2": "testpassword"}'


Login 

::

  $ curl -H "Content-Type: application/json" http://localhost:8000/api/v1/auth/login/ -d '{"username": "testusername", "password": "testpassword"}'


Getting application by API KEY

::
 
  $ curl -H "Content-Type: application/json" http://localhost:8000/api/v1/test/?api_key=API_KEY

Make sure the Application instance is pre-created through the admin or shell
