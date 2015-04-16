from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.latest, name='latest'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail')
]
