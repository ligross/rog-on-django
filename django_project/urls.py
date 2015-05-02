from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()


urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('news.urls')),
    url(r'^$', include('news.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls')),
    url(r'^articles/', include('articles.urls')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
