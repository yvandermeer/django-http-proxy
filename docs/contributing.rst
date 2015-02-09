Contributing
============

If you have any contributions, feel free to `fork Django HTTP Proxy <https://github.com/yvandermeer/django-http-proxy/fork>`_.


A `pip requirements file <http://pip.openplans.org/#requirements-files>`_ is
provided to allow easy installation of the prerequisites.

Alternatively, you can clone the Mercurial repository from Bitbucket and
manually install the package::

    $ hg clone http://bitbucket.org/yvandermeer/django-http-proxy/
    $ cd django-http-proxy
    $ python setup.py install

To automatically install the dependencies using ``pip``, you can run::

    $ pip install -r requirements.txt

    

Building the documentation
--------------------------

Documention is provided in Sphinx format in the `docs` subdirectory. To
build the HTML version of the documentation yourself, run:

    $ cd docs
    $ make html
