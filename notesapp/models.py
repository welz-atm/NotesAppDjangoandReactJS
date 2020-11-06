from django.db import models
from django.conf import settings


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    is_published = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title