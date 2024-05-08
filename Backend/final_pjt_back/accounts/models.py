from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100) 
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    class UserAgeGroup(models.TextChoices):
        AGE_GROUP_10S = '10s', '10대'
        AGE_GROUP_20S = '20s', '20대'
        AGE_GROUP_30S = '30s', '30대'

    user_age_group = models.CharField(max_length=3, choices=UserAgeGroup.choices)
    
    class ServicePurpose(models.TextChoices):
        PURPOSE_A = 'A', '서비스 목적 A'
        PURPOSE_B = 'B', '서비스 목적 B'
        # 필요한 만큼 추가할 수 있습니다.

    service_purpose = models.CharField(max_length=1, choices=ServicePurpose.choices)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    asset = models.BigIntegerField(default=0)
    auth_number = models.IntegerField(default=0)
    user_status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username