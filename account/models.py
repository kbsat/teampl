from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    nickname = models.CharField(max_length=30, null=False, blank=False)
