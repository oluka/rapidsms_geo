from django.conf.urls.defaults import *
from Map.views import main,home

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
     (r'^mapnik/', include('Mapnik.urls')),
      (r'^mapnik/', include('Mapserver.urls')),
     (r'^$',main),
     (r'^home$',home),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
     (r'^Media/(?P<path>.*)', 'django.views.static.serve',\
     {'document_root': '/home/mugisha/projects/django-projects/rapidsms_geo/Media/'}),
)
