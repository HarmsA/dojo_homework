from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.words, name='words'),
    url(r'^process/$', views.process, name='process'),
    url(r'^clear/$', views.clear, name='clear'),
]