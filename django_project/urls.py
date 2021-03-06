from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('news.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls')),
    url(r'^social/', include('social_auth.urls')),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^articles/', include('articles.urls')),
    url(r'^database/', include('database.urls')),
    url(r'^comments/', include('django_comments.urls')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
