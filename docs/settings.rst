Available settings
==================

The Django HTTP Proxy application has only a single *required* setting
(``PROXY_DOMAIN``) and a number of optional settings.

Any settings should be placed in your project's settings module (most commonly
``settings.py``).

PROXY_DOMAIN
------------
Default: Not defined

The domain that the proxy should forward to. Example::

    PROXY_DOMAIN = 'www.google.com'

PROXY_PORT
----------
Default: ``80``

The port that the proxy should forward to on the provided ``PROXY_DOMAIN``. Example::

    PROXY_PORT = 7777

PROXY_USER
----------
Default: Not defined

The username for authentication to the server that requests are forwarded to. Example::

    PROXY_USER = 'yuri'

PROXY_PASSWORD
--------------
Default: Not defined

The password for authentication to the server that requests are forwarded to. Example::

    PROXY_PASSWORD = 'secret'

.. _setting-proxy-mode:

PROXY_MODE
----------
Default: ``None``

The mode that the proxy should run in. Available modes are ``record`` and 
``play``. If no mode is defined (``None`` – the default), this means the proxy
will work as a "standard" HTTP proxy.

If the mode is set to ``record``, all requests will be forwarded to the remote
server, but both the requests and responses will be recorded to the database
for playback at a later stage::
    
    PROXY_MODE = 'record'

If the mode is set to ``play``, *no requests will be forwarded to the remote
server*.::

    PROXY_MODE = 'play'
    
In ``play`` mode, if the response (to the request being made) was previously
recorded, the recorded response will be served. Otherwise, a custom
``Http404`` exception will be raised (``RequestNotRecorded``)

PROXY_IGNORE_UNSUPPORTED
------------------------
Default: ``True``

The recording functionality of the Django HTTP Proxy is currently limited to
plain text content types. The default behavior is to ignore any unsupported
content types when ``PROXY_MODE`` is set to ``record`` – responses with
unsupported content types are not recorded and will be ignored silently. If
you set ``PROXY_IGNORE_UNSUPPORTED`` to ``False``, any unsupported response
types will raise a ``ResponseUnsupported`` exception.

PROXY_REWRITE_RESPONSES
-----------------------
Default: ``False``

Although the most common usage is probably to serve the proxy view from the
root of your project, it is also possible to prefix the proxy'd URLs::

    urlpatterns += patterns('',
        (r'^mygoogle/(?P<url>.*)$', 'httpproxy.views.proxy'),
    )

While the requests themselves will work fine, the responses may still contain
references to resources as if they were served at the root. For instance, the
Google homepage contains an ``<img>`` tag with the Google logo::

    <img alt="Google" height=110 src="/intl/en_ALL/images/logo.gif">

This would normally result in a ``404``, because there is no such URL in your
application.

By setting ``PROXY_REWRITE_RESPONSES`` to ``True``, the response will be
rewritten to try to fix the paths. In the above case, the response would now contain::

    <img alt="Google" height=110 src="/mygoogle/intl/en_ALL/images/logo.gif">

*NOTE: The rewrite logic uses a fairly simple regular expression to look for
"src", "href" and "action" attributes with a value starting with "/" – your
results may vary.*
