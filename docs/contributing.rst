Contributing
============

.. note::
    
    This project has recently moved from `Bitbucket <bitbucket_>`_ to 
    `Github <github_>`_.

If you have any contributions, feel free to
`fork Django HTTP Proxy <https://github.com/yvandermeer/django-http-proxy/fork>`_.


Development setup
-----------------

To set up the project for local development::

    $ git clone https://github.com/yvandermeer/django-http-proxy.git
    $ mkvirtualenv django-http-proxy
    $ pip install -r requirements.txt
    $ python example/manage.py syncdb
    $ python example/manage.py runserver

Finally, point your browser to http://127.0.0.1:8000/python/ and you should see 
something that resembles what you see on http://www.python.org/.


Building the documentation
--------------------------

Documention is provided in Sphinx format in the `docs` subdirectory. To
build the HTML version of the documentation yourself::

    $ cd docs
    $ make html
