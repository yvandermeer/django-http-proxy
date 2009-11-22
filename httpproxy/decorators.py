import logging

from django.conf import settings
from django.http import HttpResponse

from httpproxy.exceptions import RequestNotRecorded
from httpproxy.models import Request, Response


logger = logging.getLogger('httpproxy')
logger.setLevel(logging.DEBUG)

PROXY_CACHE_DURATION = getattr(settings, 'PROXY_CACHE_DURATION', 60 * 60 * 24) # default: 24h

def record(fn):
    """
    Records the provided request, including its parameters.
    """
    def decorate(request, url, *args, **kwargs):
        logger.info('Recording: GET "%s"' % _request_string(request))        
        recorded_request, created = Request.objects.get_or_create(
            domain=settings.PROXY_DOMAIN,
            port=settings.PROXY_PORT,
            path=request.path,
            querystring=request.GET.urlencode(),
        )
        
        # Update the timestamp on the existing recorded request
        if not created:
            recorded_request.save()
        
        # Make the actual live request as usual
        response = fn(request, url, *args, **kwargs)
        
        # Delete the previously recorded response, if any
        try:
            recorded_request.response.delete()
        except Response.DoesNotExist:
            pass
        
        # Extract the encoding from the response
        content_type = response['Content-Type']
        encoding = content_type.partition('charset=')[-1] or 'utf-8'

        # Record the new response
        Response.objects.create(
            request=recorded_request,
            status=response.status_code,
            content_type=content_type,
            content=response.content.decode(encoding), 
        )
        return response
    return decorate


def play(fn):
    
    def decorate(request, url, *args, **kwargs):
        
        try:
            matching_request = Request.objects.filter(
                domain=settings.PROXY_DOMAIN, 
                path=request.path, 
                querystring=request.GET.urlencode()
            ).latest()
        except Request.DoesNotExist, e:
            raise RequestNotRecorded('The request made has not been recorded yet. Please run httpproxy in "record" mode first.')
        
        logger.info('Playback: GET "%s"' % _request_string(request))
        response = matching_request.response # TODO handle "no response" situation
        encoding = _get_encoding(response.content_type)
        
        return HttpResponse(
            response.content.encode(encoding), 
            status=response.status, 
            mimetype=response.content_type
        )
    
    return decorate


def _get_encoding(content_type):
    return content_type.partition('charset=')[-1] or 'utf-8'

def _request_string(request):
    return '%(domain)s:%(port)d%(path)s"' % {
        'domain': settings.PROXY_DOMAIN, 
        'port': settings.PROXY_PORT, 
        'path': request.get_full_path()
    }