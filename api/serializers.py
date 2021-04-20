from rest_framework import serializers
from .models import Tag, Post


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    content = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    published_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    def get_content(self, obj):
        return obj.markdown()

    class Meta:
        model = Post
        fields = ('id', 'tags', 'title', 'thumbnail', 'content', 'description',
                  'created_at', 'updated_at', 'published_at', 'is_public')
