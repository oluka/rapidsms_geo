# Django 
from django.conf import settings
from django.http import HttpResponse

# TileCache 
from TileCache.Service import Service
from TileCache.Caches.Disk import Disk
from TileCache.Layers import Mapnik as MN
#from TileCache.Layers import WMS
#from TileCache.Layers import MapServer as MS

my_service = Service(Disk("%s" % settings.DISK_CACHE),
  {"world" : MN.Mapnik( "world", settings.MAPNIK_MAPFILE, extension = "png" ),}
  )

def tms(request):
    path_info = request.META["PATH_INFO"]
    host  = "http://" + request.META["HTTP_HOST"] + '/tiles/'
    # 'http://localhost:8000' vs. http://localhost/tilecache/tilecache.cgi
    # hack to pull off url prefix so tilecache interprets path_info correctly
    path_info = path_info.lstrip('/tms/tilecache')
    format, image = my_service.dispatchRequest( request.GET, path_info, "GET", host )
    response = HttpResponse()
    response['Content-Type'] = format
    response.write(image)
    return response

#def cache(request):
    #pass # static serve...
