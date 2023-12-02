from django.db import models
from django.utils import timezone


class Video(models.Model):
    name = models.CharField(max_length=30)
    embed_code = models.CharField(max_length=130)
    date = models.DateTimeField(blank=True, default=timezone.now)

