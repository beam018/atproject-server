from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    post_type = serializers.RelatedField()
    pub_place = serializers.RelatedField()
    pub_date = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = Post
