from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.CharField(max_length=50, blank=True)
    post_title = models.CharField(max_length=255, blank=True)
    post_text = models.TextField(blank=True)
    post_likes = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return f"{self.author}"

    def get_absolute_url(self):
        return reverse('check_post', args=(self.pk, ))
