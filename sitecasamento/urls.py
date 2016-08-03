from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^admin/', admin.site.urls),
                       url(r'', include('casamento.urls'))) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


