# Django 
from django.conf import settings
from django.http import HttpResponse

# MapServer 'mapserv' executable
from subprocess import Popen,PIPE

def wms(request):
    query_string = 'QUERY_STRING=map=%s&%s' % ( settings.MAPSERVER_MAPFILE, request.META['QUERY_STRING'] )
    im = Popen(['mapserv',query_string],stdin=PIPE,stdout=PIPE)
    image = im.stdout.read()
    im.stdout.close()
    mime = request.GET['FORMAT']
    image = image.replace('Content-type: %s\n\n' % str(mime),'')
    response = HttpResponse()
    response['Content-length'] = len(image)
    response['Content-Type'] = mime
    response.write(image)
    return response