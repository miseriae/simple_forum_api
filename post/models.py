from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

from vote.models import Vote


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    vote = GenericRelation(Vote)

    def __str__(self):
        return self.title

    @property
    def total_votes(self):
        return self.vote.count()
