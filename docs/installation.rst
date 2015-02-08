Installation
============

Requirements
------------

Django HTTP Proxy is compatible with Python 2.5.x and Python 2.6.x. It was
testing with Django 1.1.1, but should work on earlier releases as well. In
addition, the package depends on the httplib2 python package.

A `pip requirements file <http://pip.openplans.org/#requirements-files>`_ is
provided to allow easy installation of the prerequisites.

Download & Install
------------------

Django HTTP Proxy is `available on the Python Package Index <http://pypi.python.org/pypi/django-http-proxy>`_.

As such, you can easily install the latest release using
`easy_install <http://pypi.python.org/pypi/setuptools>`_::

    $ easy_install django-http-proxy

or using `pip <http://pypi.python.org/pypi/pip>`_::

    $ pip install django-http-proxy

Alternatively, you can clone the Mercurial repository from Bitbucket and
manually install the package::

    $ hg clone http://bitbucket.org/yvandermeer/django-http-proxy/
    $ cd django-http-proxy
    $ python setup.py install

To automatically install the dependencies using ``pip``, you can run::

    $ pip install -r requirements/libs.txt

Configuration
-------------

After you've installed the ``django-http-proxy`` package to your site-packages
directory (or any other location on your python path), you need to add
``httpproxy`` to your installed app in the Django ``settings.py`` file::

    INSTALLED_APPS = (
        ...
        'httpproxy',
    )

Next, you should run ``syncdb`` to create the necessary database tables::

    $ ./manage.py syncdb

To use Django HTTP Proxy, you create an entry in your ``urls.py`` that forwards
requests to the ``httpproxy.views.HttpProxy`` view class, e.g.::

    from httpproxy.views import HttpProxy

    urlpatterns += patterns('',
        (r'^(?P<url>.*)$', HttpProxy.as_view(base_url = settings.PROXY_BASE_URL)),
    )
    
Given the above url config, all requests will be forwarded to the ``proxy``
view function. The domain to which the proxy will forward request can be
configured using the ``PROXY_BASE_URL`` setting::

    PROXY_BASE_URL = 'http://www.google.com'

For a complete overview of possible settings, see :doc:`settings`.
