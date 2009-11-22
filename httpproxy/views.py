import httplib2
 
from django.http import HttpResponse

from httpproxy import settings
from httpproxy.exceptions import UnkownProxyMode
 

PROXY_FORMAT = u'http://%s:%d/%s' % (settings.PROXY_DOMAIN, settings.PROXY_PORT, u'%s')

def proxy(request, url):
    conn = httplib2.Http()
    
    # Optionally provide authentication for server
    try:
        conn.add_credentials(settings.PROXY_USER, settings.PROXY_PASSWORD)
    except AttributeError:
        pass
    
    if request.method == 'GET':
        url_ending = '%s?%s' % (url, request.GET.urlencode())
        url = PROXY_FORMAT % url_ending
        response, content = conn.request(url, request.method)
    elif request.method == 'POST':
        url = PROXY_FORMAT % url
        data = request.POST.urlencode()
        response, content = conn.request(url, request.method, data)
    return HttpResponse(content, status=int(response['status']), mimetype=response['content-type'])


if settings.PROXY_MODE is not None:
    proxy_mode = settings.PROXY_MODE
    try:
        decorator = getattr(__import__(__package__ + '.decorators', fromlist=proxy_mode), proxy_mode)
    except AttributeError, e:
        raise UnkownProxyMode('The proxy mode "%s" could not be found. Please specify a corresponding decorator function in "%s.decorators".' % (proxy_mode, __package__))
    else:
        proxy = decorator(proxy)
    
