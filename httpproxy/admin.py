from django.contrib import admin

from httpproxy.models import Request, Response


class ResponseInline(admin.StackedInline):
    model = Response

class RequestAdmin(admin.ModelAdmin):
    list_display = ('domain', 'port', 'path', 'querystring', 'date')
    list_filter = ('domain', 'port')
    inlines = [ResponseInline,]

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('request_domain', 'request_path', 'request_querystring', 'status', 'content_type')
    list_filter = ('status', 'content_type')


admin.site.register(Request, RequestAdmin)
admin.site.register(Response, ResponseAdmin)
