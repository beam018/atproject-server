from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.csrf import csrf_exempt
from mailer.views import MailView
import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^mail/$', csrf_exempt(MailView.as_view())),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^v1/projects/', include('projects.urls')),
    (r'^v1/jobs/', include('career.urls')),
    (r'^v1/pages/', include('pages.urls')),
)

urlpatterns += patterns('',
    (r'^ckeditor/', include('ckeditor.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT}),
    )
