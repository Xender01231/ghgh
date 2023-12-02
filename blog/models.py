from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=30)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(blank=True, default=timezone.now)
    images = models.ImageField(upload_to='images/', blank=True)