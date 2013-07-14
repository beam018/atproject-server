from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from pages.models import Page
from pages.serializers import PageSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'pages': reverse('pages-view', request=request),
    })


class PagesView(generics.ListAPIView):
    serializer_class = PageSerializer

    def get_queryset(self):
        queryset = Page.objects.filter(type=self.kwargs['type']).order_by('order_number')

        return queryset