from django.conf import settings

from httpproxy.recorder import ProxyRecorder


PROXY_CACHE_DURATION = getattr(settings, 'PROXY_CACHE_DURATION', 60 * 60 * 24) # default: 24h

recorder = ProxyRecorder()

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
