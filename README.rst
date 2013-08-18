An application which works with Google OAuth2 and with Calendar API.

Run
===

Get ``buildout``::

    python bootstrap.py

Create project structure::

    bin/buildout

Make sure ``EVENT_CREATOR_SECRET_KEY`` environment variable is set::

    export EVENT_CREATOR_SECRET_KEY="something secret"
    
Make sure ``EVENT_CREATOR_OAUTH_CLIENT_ID`` environment variable is set
which is Client ID to access Google APIs::

    export EVENT_CREATOR_OAUTH_CLIENT_ID="client id"
    
Make sure ``EVENT_CREATOR_OAUTH_CLIENT_SECRET`` environment variable is
set which is Client secret used to access Google APIs::

    export EVENT_CREATOR_OAUTH_CLIENT_SECRET="client secret"
    
Make sure that calendar is enabled in Google APis console (https://code.google.com/apis/console).

Setup database and create superuser::

    bin/django syncdb

Run application (application is accessible at http://localhost:8000)::

    bin/django runserver

Tests
=====

Unit tests are placed in directory ``src/event_creator/tests``.

The pattern for test filename is ``*_tests.py``.

Run only unit tests::

    bin/unit-tests

Run unit tests, check pep8 and pyflakes::

    bin/check
    
To run functional tests there must be provided test account for Google::

    export EVENT_CREATOR_TEST_EMAIL="email"
    export EVENT_CREATOR_TEST_EMAIL_PASSWORD="password"
    
Run functional tests::

    bin/functional_tests
