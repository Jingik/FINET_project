from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'phone_number', 'user_age_group', 'service_purpose', 'account_number', 'asset', 'auth_number', 'user_status']
        extra_kwargs = {
            'password': {'write_only': True},  # 패스워드는 읽기 전용으로 설정하여 노출을 방지합니다.
        }
