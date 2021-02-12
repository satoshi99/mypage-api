from django.db.models import Count, Q
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer, TagSerializer
from .models import Post, Tag


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 9


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
