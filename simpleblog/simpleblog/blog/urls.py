from django.urls import include, path
from .views import PostListView, PostDetailView

app_name = "simpleblog.blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]

