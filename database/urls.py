from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.content_page, name='content_page'),
    url(r'^(?P<page_id>[0-9]+)/$', views.page, name='page')
]