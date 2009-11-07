django-tiles
-------------

Proof of concept examples for generating map tiles within Django.

To test this application download the django-tiles folder

 - Then from within the django-tiles folder run::
 
 $ python manage.py runserver

To enable this application within a larger Django Project:
 
 - Clone the django-tiles hg repository.

 - Put the `tiles` folder inside on your PYTHONPATH

 - Or just copy or symlink the `tiles` folder into your project folder.
 
 - Add `tiles` to your INSTALLED APPS.

To run each example map tile engine you must install a dependency:

MapServer::

$ sudo apt-get install python-mapscript

Mapnik::

$ sudo apt-get install python-mapnik

Nik2img::

$ sudo easy_install http://mapnik-utils.googlecode.com/svn/trunk/nik2img/

or

$ sudo easy_install http://mapnik-utils.googlecode.com/svn/trunk/nik2img/

TileCache::

$ sudo pip install http://svn.tilecache.org/trunk/tilecache/

or

$ sudo easy_install http://svn.tilecache.org/trunk/tilecache/

More info
---------

http://www.bitbucket.org/springmeyer/django-tiles/