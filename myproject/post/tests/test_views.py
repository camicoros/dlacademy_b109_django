import os

from django.test import TestCase
from django.urls import reverse

from core.models import CustomUser
from post.models import Post


class TestIndexView(TestCase):

    def test_empty_index(self):
        response = self.client.get(reverse('post:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Постов нет!')

    def test_index_with_view(self):
        user1 = CustomUser.objects.create(
            username="root",
            password="root",
            avatar=os.path.join("test_media", "01.png")
        )
        post = Post.objects.create(
            author=user1,
            image=os.path.join("test_media", "01.png"),
            title="First post"
        )
        response = self.client.get(reverse('post:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['posts'], [post])