from django.conf.urls import include, url
from . import views


urlpatterns = [ url(r'^$', views.tela_inicial),
                url(r'^local', views.local_casamento),
                url(r'^listapresentes', views.linkpresente),
                url(r'^presenca', views.presenca),
                url(r'^contato', views.contato),
                url(r'^confirma/$', views.postconfirmacao),
                url(r'^agradecimento/$', views.agradecimento),]
