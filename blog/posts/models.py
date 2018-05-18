from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.id, ))
