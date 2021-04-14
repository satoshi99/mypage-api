from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, response
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer, TagSerializer
from .models import Post, Tag



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return response.Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total': self.page.paginator.num_pages,
            'current': self.page.number,
            'results': data,
        })


class PostListView(generics.ListAPIView):
    queryset = Post.objects.filter(is_public=True)
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        tag = get_object_or_404(Tag, slug=tag_slug)
        qs = super().get_queryset().filter(tags=tag)
        return qs


class SearchPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        lookups = (
            Q(tags__name__icontains=query) |
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(content__icontains=query)
        )
        if query is not None:
            qs = super().get_queryset().filter(lookups).distinct()
            return qs
        qs = super().get_queryset()
        return qs