from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from pages.views import PageView

urlpatterns = patterns('projects.views',
    url(r'^(?P<name>\w+)/$', PageView.as_view()),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
