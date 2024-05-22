from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

        
class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'id', 'username', 'password', 'password_confirm', 'name', 
            'phone_number', 'email', 'user_age_group', 'service_purpose', 
            'asset'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        validated_data['password'] = make_password(validated_data['password'])
        user = super(UserSerializer, self).create(validated_data)

        return user

    def update(self, instance, validated_data):
        instance = super(UserSerializer, self).update(instance, validated_data)
        return instance
