from httpproxy import settings
from httpproxy.recorder import ProxyRecorder


proxy = ProxyRecorder(settings.PROXY_DOMAIN, settings.PROXY_PORT)

def record(fn):
    """
    Decorator for recording the request being made and its response.
    """
    def decorate(request, url, *args, **kwargs):
        
        # Make the actual live request as usual
        response = fn(request, url, *args, **kwargs)
        
        # Record the request and response
        proxy.record(request, response)

        return response
    return decorate


def play(fn):
    """
    Decorator for playing back the response to a request, based on a
    previously recorded request/response.
    """
    def decorate(request, url, *args, **kwargs):
        return proxy.playback(request)
        
    return decorate
