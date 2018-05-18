from django.apps import apps
from django.test import TestCase
from posts.apps import PostsConfig


class PostsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(PostsConfig.name, 'posts')
        self.assertEqual(apps.get_app_config('posts').name, 'posts')
