from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from posts.models import Post, PostType, PostPlace
from posts.serializers import PostSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('posts-view', request=request),
    })


class PostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-pub_date')
        return queryset
