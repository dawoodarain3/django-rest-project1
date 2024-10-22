from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_type = models.CharField(max_length=10,null=False)
    roll = models.IntegerField(null=True)
    city = models.CharField(max_length=100)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return f'{self.username}'