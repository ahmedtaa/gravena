# yossry add how to setup  #
===================================================

gravena
==============================

Gravena website

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django



Settings
------------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

* Install python 3 package manager::

   $ sudo apt-get install python3-pip

* Install virtualenv for creating isolated environments for projects (So packages are not system-wide)::

   $ sudo python3 -m pip install virtualenv

* Create isolated environment for gravena project (Don't track it in git)::

   $ python3 -m virtualenv gravena-env

* Activate that environment for your terminal session(You'll need to do that everytime you'll work on project, and for every new terminal session)::

   $ source gravena-env/bin/activate
You should see difference in your terminal

* Enter the project Directory::

   $ cd "site directory"

* Install requirements::

   $ python3 -m pip install -r requirements/local.txt 

* Migrate the DB::

   $ python3 manage.py migrate.
   

# Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


* install npm packages::

   $ sudo npm install

* Run The development server::

   $ python3 manage.py runserver
   $ grunt serve

You should be able to visit the website at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test


Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html









Deployment
----------

$ git checkout gravena/static
$ git pull --rebase origin master
$ grunt build
$ python manage.py collectstatic
$ supervisorctl restart gravina



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html