from django.test import TestCase

from posts.models import Post


class PostModelTests(TestCase):
    def test_dunder_str(self):
        post = Post(title='Test Title', description='Test Description')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        post = Post.objects.create(title='Test Title', description='Test Description')
        self.assertEqual(post.get_absolute_url(), f'/posts/{post.id}/')
