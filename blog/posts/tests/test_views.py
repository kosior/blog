from django.test import TestCase

from django.shortcuts import reverse

from posts.models import Post
from posts.forms import BlogPostForm


class PostListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_list.html')

    def test_message_displayed_when_no_posts(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'No blog posts found.')

    def test_lists_all_posts(self):
        Post.objects.bulk_create(
            [Post(title=f'Test Title {i}', description=f'Test description {i}') for i in range(10)]
        )
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['posts']) == 10)

    def test_displays_all_posts(self):
        Post.objects.bulk_create(
            [Post(title=f'Test Title {i}', description=f'Test description {i}') for i in range(10)]
        )
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        [self.assertContains(response, f'Test Title {i}') for i in range(10)]

    def test_if_links_to_detail_view_exsits(self):
        posts = [Post.objects.create(title='Test Title', description='Test description') for _ in range(3)]
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        [self.assertContains(response, post.get_absolute_url()) for post in posts]


class PostDetailViewTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Test Title', description='Test description')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/posts/{self.post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('posts:detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('posts:detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_detail.html')

    def test_no_post(self):
        response = self.client.get(reverse('posts:detail', args=[12345]))
        self.assertEqual(response.status_code, 404)

    def test_post_exists(self):
        response = self.client.get(reverse('posts:detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Title')
        self.assertContains(response, 'Test description')

    def test_if_edit_link_exists(self):
        response = self.client.get(reverse('posts:detail', args=[self.post.id]))
        self.assertContains(response, self.post.get_absolute_url() + 'update/')


class PostCreateViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/posts/create/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('posts:create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('posts:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_form.html')

    def test_correct_form_in_context(self):
        response = self.client.get(reverse('posts:create'))
        self.assertTrue(isinstance(response.context['form'], BlogPostForm))

    def test_add_new_post(self):
        response = self.client.post(reverse('posts:create'),
                                    {'title': 'Test Title 123', 'description': 'Test description 123'})
        self.assertEqual(response.status_code, 302)
        created_post = Post.objects.get(title='Test Title 123')
        self.assertTrue(created_post.description == 'Test description 123')


class PostUpdateViewTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Test Title', description='Test description')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/posts/{self.post.id}/update/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('posts:update', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('posts:update', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_form.html')

    def test_correct_form_in_context(self):
        response = self.client.get(reverse('posts:update', args=[self.post.id]))
        self.assertTrue(isinstance(response.context['form'], BlogPostForm))

    def test_display_post(self):
        response = self.client.get(reverse('posts:update', args=[self.post.id]))
        self.assertContains(response, 'Test Title')
        self.assertContains(response, 'Test description')

    def test_if_updated(self):
        response = self.client.post(reverse('posts:update', args=[self.post.id]),
                                    {'title': 'Updated Title', 'description': 'Updated description'})
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.description, 'Updated description')
