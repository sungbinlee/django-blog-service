from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from blogservice.utils import uuid_name_upload_to

"""
Auth User Model
- 생성
- 삭제
- 수정
--> UserManager Helper class 
"""


class UserManager(BaseUserManager):
    def _create_user(
        self, email, password, is_staff, is_superuser, is_active, **extra_fields
    ):
        if not email:
            raise ValueError("User must have an email")
        now = timezone.localtime()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create_user
    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    # created_superuser
    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=50, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    data_joined = models.DateTimeField(auto_now_add=True)
    social_provider = models.CharField(max_length=255, blank=True)
    social_id = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to=uuid_name_upload_to, blank=True)
    introduction = models.TextField(blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    # def __str__(self):
    #     return self.name
