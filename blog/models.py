from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    text = HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:250] + "..."