from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.CharField(max_length=30)
    text = models.TextField(max_length=10000, null=True)

    def __str__(self):
        return self.author


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def save(self, **kwargs):
        self.created_at = timezone.now() - timedelta(days=364)
        super().save(**kwargs)

    def __str__(self):
        return "{} by {}".format(self.post, self.user.username)
