from django.db import models

from core.models import CustomUser
from django.urls import reverse
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    tag = models.ForeignKey(Tag, related_name='posts', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    date_pub = models.DateTimeField(default=timezone.now)
    date_edit = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts', blank=True)

    def __str__(self):
        return f"Post from {self.author.username}"

    def get_absolute_url(self):
        return reverse('post:detail', args=(self.id, ))

    # @property
    # def get_likes(self):
    #     return self.likes.count()


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_pub = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment from {self.author.username} to {self.post.title}"

