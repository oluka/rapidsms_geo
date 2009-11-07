from django.conf import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext

engines = {}
methods = {}
  
try:
    import mapnik_engine
    engines['mapnik'] = mapnik_engine
    methods['mapnik'] = ['wms','gmaps']
except ImportError, E:
    print 'Unable to import tile engine:\n %s' % E

try:
    import nik2img_engine
    engines['nik2img'] = mapnik_engine
    methods['nik2img'] = ['wms']
except ImportError, E:
    print 'Unable to import tile engine:\n %s' % E
    
try:
    import mapscript_engine
    engines['mapscript'] = mapscript_engine
    methods['mapscript'] = ['wms']
except ImportError, E:
    print 'Unable to import tile engine:\n %s' % E

try:
    import mapserv_engine
    engines['mapserv'] = mapserv_engine
    methods['mapserv'] = ['wms']
except ImportError, E:
    print 'Unable to import tile engine:\n %s' % E

try:
    import tilecache_engine
    engines['tilecache'] = tilecache_engine
    methods['tilecache'] = ['wms','tms','tms-force','cache']
except ImportError, E:
    print 'Unable to import tile engine:\n %s' % E


# TODO weave dicts into auto index html of possible pages
def home(request):
    return render_to_response('home.html', RequestContext(request,{}))

def tiles_dispatcher(request, method, engine):
    global engines
    global methods
    tile_engine = engines.get(engine)
    responder = getattr(tile_engine,method)
    if tile_engine and method in methods[engine]:
      return getattr(tile_engine,method)(request)

def map_client(request, method, engine):
    return render_to_response('tiles.html',
        RequestContext(request, {'method':method,'engine':engine} ) )