from rest_framework import serializers
from simpleblog.blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer class for the `Post` model.
    This class handles the serialization of the `Post` model data.
    """

    class Meta:
        model = Post
        fields = ["title", "slug", "author", "body", "status", "publish"]

