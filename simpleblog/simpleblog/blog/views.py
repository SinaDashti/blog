from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator, EmptyPage

from .models import Post, PostStatus


class CustomPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if number > 1:
                return self.num_pages
            if number < 1:
                return 1
            else:
                raise


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/list.html"
    paginator_class = CustomPaginator

    def get_queryset(self):
        """Just the published post should be returned"""
        return super().get_queryset().filter(status=PostStatus.PUBLISHED)


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/detail.html"

