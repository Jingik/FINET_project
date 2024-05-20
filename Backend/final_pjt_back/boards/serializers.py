# serializers.py
from rest_framework import serializers
from .models import Board, Comment
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'phone_number', 'email', 'user_age_group', 'service_purpose', 'asset']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_name', 'user_id', 'board', 'parent_comment', 'content', 'created_at', 'updated_at']
        read_only_fields = ['user', 'board', 'created_at', 'updated_at']

class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'user', 'user_name', 'title', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['user', 'created_at', 'updated_at']
