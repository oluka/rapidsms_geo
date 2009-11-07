# Create your views here.
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, \
    HttpResponseNotAllowed, Http404, HttpResponse, HttpResponseBadRequest, \
    HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render_to_response
def main(request):
    return render_to_response('index.html')
def home(request):
    return render_to_response('index2.html')
from TileCache.Service import Service



def get_tile(request):
    global _service

    format, image = _service.dispatchRequest(
        request.GET, request.path, request.method, 
        request.get_host())
    result = HttpResponse(str(image), mimetype=format)
    return result
    