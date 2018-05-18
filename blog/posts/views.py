from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .forms import BlogPostForm
from .models import Post


class PostDetail(DetailView):
    model = Post


class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class PostCreate(CreateView):
    model = Post
    form_class = BlogPostForm


class PostUpdate(UpdateView):
    model = Post
    form_class = BlogPostForm
