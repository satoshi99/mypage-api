from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from . import models
from . import serializers

BLOG_URL = '/api/'
POST_DETAIL_URL = '/api/post/'
TAGS_URL = '/api/tags/'


def create_tag(name, slug):
    return models.Tag.objects.create(name=name, slug=slug)

def create_post(tags, title, thumbnail, content, description, is_public):
    return models.Post.objects.create(
        tags=tags,
        title=title,
        thumbnail=thumbnail,
        content=content,
        description=description,
        is_public=is_public
    )

def detail_url(post_id):
    return reverse('api:post-detail', args=[post_id])


class ApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_should_get_all_tags(self):
        create_tag(name='Python', slug='python')
        create_tag(name='Django', slug='django')
        res = self.client.get(TAGS_URL)
        tags = models.Tag.objects.all().order_by('id')
        serializer = serializers.TagSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_should_get_all_posts(self):
        tag1 = create_tag(name='Python', slug='python')
        tag2 = create_tag(name='Django', slug='django')
        create_post(tags=[tag1], title='dummy_title1', thumbnail='dummy_thumbnail1.jpg',
                    content='dummy_content1', description='dummy_description1', is_public=True)
        create_post(tags=[tag2], title='dummy_title2', thumbnail='dummy_thumbnail2.jpg',
                    content='dummy_content2', description='dummy_description2', is_public=False)
        res = self.client.get(BLOG_URL)
        posts = models.Post.objects.all().order_by('id')
        serializer = serializers.Post(posts)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_should_get_single_post(self):
        tag1 = create_tag(name='Python', slug='python')
        tag2 = create_tag(name='Django', slug='django')
        post = create_post(tags=[tag1, tag2], title='dummy_title2', thumbnail='dummy_thumbnail2.jpg',
                           content='dummy_content2', description='dummy_description2', is_public=False)
        url = detail_url(post.id)
        res = self.client.get(url)
        serializer = serializers.Post(post)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)




