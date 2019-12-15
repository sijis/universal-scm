Universal SCM
=============

The multilingual Python API for accessing popular SCM REST APIs.

Installation
------------

.. code-block:: bash

    virtualenv venv
    source venv/bin/activate

    pip install .

Usage
-----

.. code-block:: python

    import universalscm

    GITHUB_TOKEN = 'secret'

    scm = universalscm.UniversalSCM(
        provider='github',
        version='v3',
        token=GITHUB_TOKEN,
    )

    user = scm.user()
    print(user['login'])
