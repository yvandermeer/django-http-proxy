import httplib2
from urllib import urlencode
 
from django.conf import settings
from django.http import HttpResponse
 

try:
    PROXY_DOMAIN = getattr(settings, 'PROXY_DOMAIN')
except AttributeError:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured("To use the 'httpproxy' app, please add the PROXY_DOMAIN setting to your settings file.")

PROXY_PORT = getattr(settings, 'PROXY_PORT', 80)

PROXY_FORMAT = u'http://%s:%d/%s' % (PROXY_DOMAIN, PROXY_PORT, u'%s')

def proxy(request, url):
    conn = httplib2.Http()
    
    # Optionally provide authentication for server
    try:
        conn.add_credentials(settings.PROXY_USER, settings.PROXY_PASSWORD)
    except AttributeError:
        pass
    
    if request.method == 'GET':
        url_ending = '%s?%s' % (url, urlencode(request.GET))
        url = PROXY_FORMAT % url_ending
        response, content = conn.request(url, request.method)
    elif request.method == 'POST':
        url = PROXY_FORMAT % url
        data = urlencode(request.POST)
        response, content = conn.request(url, request.method, data)
    return HttpResponse(content, status=int(response['status']), mimetype=response['content-type'])
    
