from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    social_provider = models.CharField(max_length=255, blank=True, null=True)
    social_id = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username