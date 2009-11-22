from httpproxy import settings
from httpproxy.recorder import ProxyRecorder


recorder = ProxyRecorder(settings.PROXY_DOMAIN, settings.PROXY_PORT)

def record(fn):
    """
    Decorator for recording the request being made and its response.
    """
    def decorate(request, url, *args, **kwargs):
        recorded_request = recorder.record_request(request)
        
        # Make the actual live request as usual
        response = fn(request, url, *args, **kwargs)
        
        recorder.record_response(recorded_request, response)

        return response
    return decorate


def play(fn):
    """
    Decorator for playing back the response to a request, based on a
    previously recorded request/response.
    """
    def decorate(request, url, *args, **kwargs):
        return recorder.playback_response(request)
        
    return decorate
