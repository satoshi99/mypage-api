from django.urls import path
from api.views import PostListView, PostRetrieveView, TagListView


urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('post/<int:pk>', PostRetrieveView.as_view(), name='post_detail'),
    path('tags/', TagListView.as_view(), name='tag_list'),
]
