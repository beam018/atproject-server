from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from posts.views import PostsView

urlpatterns = patterns('posts.views',
    url(r'^$', PostsView.as_view(), name='post-list'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
