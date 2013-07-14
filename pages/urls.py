from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from pages.views import PagesView

urlpatterns = patterns('pages.views',
    url(r'^(?P<type>\w+)/$', PagesView.as_view(), name='project-list'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])