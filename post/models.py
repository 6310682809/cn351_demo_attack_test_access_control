from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from user.models import *
# Create your models here.

class Post(models.Model):
    created_by = models.ForeignKey(
        UserInfo, on_delete=models.CASCADE, related_name='post_by')
    detail = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f'{ self.created_by.user } post { self.detail }'
