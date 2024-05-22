from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field is required')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    user_age_group = models.CharField(max_length=3, choices=[
        ('10대', '10대'),
        ('20대', '20대'),
        ('30대', '30대'),
        ('40대', '40대'),
        ('50대', '50대')
    ])
    service_purpose = models.CharField(max_length=10, choices=[
        ('예금 가입', '예금 가입'),
        ('적금 가입', '적금 가입'),
        ('대출 가입', '대출 가입')
    ])
    asset = models.BigIntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
