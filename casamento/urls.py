from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.tela_inicial),
    url(r'^local', views.local_casamento),
    url(r'^listapresentes', views.listapresentes),
    url(r'^presenca', views.presenca)
)
