from django.db import models
from django.contrib.auth.models import User

from post.models import Post


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=512)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.body
