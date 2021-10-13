
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.conf.urls.static import static
from django.conf import settings


import photoalbum

#_____CHANGE ADMIN PANEL_____
admin.site.site_header = 'A awesome Site'
admin.site.site_title = 'Album'
admin.site.index_title = 'Some album'




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photoalbum.urls',namespace='photoalbum')),

]


#ami for static foder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                   document_root = settings.MEDIA_ROOT)
