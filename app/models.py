import datetime
from django.db import models
from django.utils import timezone
class Tweet(models.Model):
    content = models.CharField(max_length=280)
    time_created = models.DateTimeField(default=timezone.now())
    creator = models.CharField(max_length=50)