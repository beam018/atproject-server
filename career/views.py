from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from career.models import JobCategory, Job, City
from career.serializers import JobCategorySerializer, JobSerializer, CitySerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'jobs': reverse('job-list', request=request),
        'cities': reverse('city-list', request=request),
        'categories': reverse('jobcategory-list', request=request),
    })


class CityList(generics.ListAPIView):
    model = City
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveAPIView):
    model = City
    serializer_class = CitySerializer


class JobCategoryList(generics.ListAPIView):
    model = JobCategory
    serializer_class = JobCategorySerializer


class JobCategoryDetail(generics.RetrieveAPIView):
    model = JobCategory
    serializer_class = JobCategorySerializer


class JobList(generics.ListAPIView):
    model = Job
    serializer_class = JobSerializer

    def get_queryset(self):
        return self.model.objects.filter(status='p')


class JobDetail(generics.RetrieveAPIView):
    model = Job
    serializer_class = JobSerializer
