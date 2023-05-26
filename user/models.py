from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    role = models.CharField(max_length=15)

    
    def __str__(self):
        return f'{ self.user} {self.role}'