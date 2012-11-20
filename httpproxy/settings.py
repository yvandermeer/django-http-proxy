from django.conf import settings
"""
Settings wrapper for Django HTTP Proxy.

Provides defaults and sensible error messages for settings used by the
'httpproxy' application.
"""

PROXY_PORT = getattr(settings, 'PROXY_PORT', 80)

# Optional authentication
if hasattr(settings, 'PROXY_USER') and hasattr(settings, 'PROXY_PASSWORD'):
    PROXY_USER = settings.PROXY_USER
    PROXY_PASSWORD = settings.PROXY_PASSWORD

PROXY_IGNORE_UNSUPPORTED = getattr(settings, 'PROXY_IGNORE_UNSUPPORTED', True)

PROXY_REWRITE_RESPONSES = getattr(settings, 'PROXY_REWRITE_RESPONSES', False)
