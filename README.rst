Example App: Django with Dropbox
================================

This is an example Django_ app with Dropbox_ integration, via
`Python Social Auth`_. It is a Procfile-based application, so it can run
on Heroku_ easily.

To run it locally, you'll need an OAuth 2 key and secret from Dropbox. You
can get those by `creating an app on Dropbox`_. Once you have them, copy
the ``.env.example`` file to ``.env`` and put the key and secret into that
file.

Install all the application's dependencies (specified in the
``requirements.txt`` file). Then install honcho_, and use it to run the
Procfile locally.

.. code-block:: bash

    pip install -r requirements.txt
    pip install honcho
    honcho start

Then visit ``http://localhost:5000/`` to view the application.

.. _Django: https://www.djangoproject.com/
.. _Dropbox: https://www.dropbox.com/
.. _Python Social Auth: http://python-social-auth.readthedocs.io/en/latest/
.. _Heroku: https://www.heroku.com/
.. _creating an app on Dropbox: https://www.dropbox.com/developers/apps/create
.. _honcho: https://github.com/nickstenning/honcho
