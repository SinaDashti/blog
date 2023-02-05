from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from simpleblog.blog.models import Post, PostStatus

from .serializers import PostSerializer

# TODO move to another file
class UserIsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission class to allow only authors of a post or superuser to edit a post.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_superuser:
            return obj.author == request.user
        return True


class PostViewset(ModelViewSet):
    """
    ViewSet class to handle CRUD operations for `Post` model.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_permissions(self):
        """
        Override the default permission classes for update and delete methods.

        Returns:
        - A list of permission classes to be applied for the current request.
        """
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [
                UserIsAuthorOrReadOnly,
            ]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        """
        Filter the `Post` queryset to return only published posts.

        Returns:
        - The filtered queryset of `Post` model.
        """
        return super().get_queryset().filter(status=PostStatus.PUBLISHED)

