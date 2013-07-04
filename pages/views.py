from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from pages.models import Page, PageType
from pages.serializers import PageSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        '': reverse('page-view', request=request),
    })


class PageView(generics.ListAPIView):
    serializer_class = PageSerializer

    def get_queryset(self):
        type = PageType.objects.get(name=self.kwargs['name'])
        queryset = Page.objects.filter(type=type)

        return queryset