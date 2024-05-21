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

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    interest_rate = models.FloatField()

    def __str__(self):
        return self.name

class UserProduct(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    user_age_group = models.CharField(max_length=3, choices=[
        ('10s', '10대'),
        ('20s', '20대'),
        ('30s', '30대'),
        ('40s', '40대'),
        ('50s', '50대')
    ])
    service_purpose = models.CharField(max_length=1, choices=[
        ('A', '서비스 목적 A'),
        ('B', '서비스 목적 B'),
        ('C', '서비스 목적 C')
    ])
    asset = models.BigIntegerField(default=0)
    subscribed_products = models.ManyToManyField(Product, through=UserProduct, related_name='subscribers')

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
