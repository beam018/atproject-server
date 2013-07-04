from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from projects.models import Project
from projects.serializers import ProjectSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'projects': reverse('project-list', request=request),
    })


class ProjectList(generics.ListAPIView):
    model = Project
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveAPIView):
    model = Project
    serializer_class = ProjectSerializer
