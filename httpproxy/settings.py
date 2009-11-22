from django.conf import settings
"""
Settings wrapper for Django HTTP Proxy.

Provides defaults and sensible error messages for settings used by the
'httpproxy' application.
"""

try:
    PROXY_DOMAIN = getattr(settings, 'PROXY_DOMAIN')
except AttributeError:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured("To use the 'httpproxy' app, please add the PROXY_DOMAIN setting to your settings module.")

PROXY_PORT = getattr(settings, 'PROXY_PORT', 80)

# Optional authentication
if hasattr(settings, 'PROXY_USER') and hasattr(settings, 'PROXY_PASSWORD'):
    PROXY_USER = settings.PROXY_USER
    PROXY_PASSWORD = settings.PROXY_PASSWORD

PROXY_MODE = getattr(settings, 'PROXY_MODE', None)
