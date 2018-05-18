from django.test import TestCase

from posts.forms import BlogPostForm


class BlogPostFormTest(TestCase):
    def test_css_class(self):
        form = BlogPostForm()
        for field in form.fields.values():
            self.assertTrue(field.widget.attrs['class'] == 'form-control')

    def test_form_valid(self):
        form = BlogPostForm(data={'title': 'Title', 'description': 'Description'})
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = BlogPostForm(data={'title': '', 'description': ''})
        self.assertFalse(form.is_valid())
