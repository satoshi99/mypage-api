from django.urls import path
from api.views import PostListView, PostRetrieveView, TagListView, TagPostView, SearchPostView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='blog'),
    path('posts/<int:pk>', PostRetrieveView.as_view(), name='post_detail'),
    path('posts/search/', SearchPostView.as_view(), name='search_posts'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tags/<str:tag_slug>', TagPostView.as_view(), name='tag_posts'),
]
