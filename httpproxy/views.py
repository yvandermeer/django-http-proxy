import httplib2
from urllib import urlencode
 
from django.conf import settings
from django.http import HttpResponse
 
 
PROXY_FORMAT = u"http://%s:%d/%s" % (settings.PROXY_DOMAIN, settings.PROXY_PORT, u"%s")

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
        resp, content = conn.request(url, request.method)
        return HttpResponse(content, mimetype=resp['content-type'])
    elif request.method == 'POST':
        url = PROXY_FORMAT % url
        data = urlencode(request.POST)
        resp, content = conn.request(url, request.method, data)
        return HttpResponse(content)