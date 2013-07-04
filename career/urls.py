from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from career.views import JobCategoryList, JobCategoryDetail, JobList, JobDetail, CityList, CityDetail

urlpatterns = patterns('career.views',
    url(r'^$', JobList.as_view(), name='job-list'),
    url(r'^(?P<pk>\d+)/$', JobDetail.as_view(), name='job-detail'),

    url(r'^cities/$', CityList.as_view(), name='city-list'),
    url(r'^cities/(?P<pk>\d+)/$', CityDetail.as_view(), name='city-detail'),

    url(r'^categories/$', JobCategoryList.as_view(), name='jobcategory-list'),
    url(r'^categories/(?P<pk>\d+)/$', JobCategoryDetail.as_view(), name='jobcategory-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])