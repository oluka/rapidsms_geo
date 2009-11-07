from django.conf.urls.defaults import *
from django.conf import settings
from views import *

urlpatterns = patterns('',

    (r'^$', home),
    (r'^map/(?P<method>\w+)/(?P<engine>\w+)/$', map_client),
    (r'^cache/tilecache/(.*)$','django.views.static.serve',{'document_root': settings.DISK_CACHE, 'show_indexes': True}),
    (r'^(?P<method>\w+)/(?P<engine>\w+)/(.*)$', tiles_dispatcher),    
    )
