from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from projects.views import ProjectList, ProjectDetail

urlpatterns = patterns('projects.views',
    url(r'^$', ProjectList.as_view(), name='project-list'),
    url(r'^(?P<pk>\d+)/$', ProjectDetail.as_view(), name='project-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])