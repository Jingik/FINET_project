from rest_framework import serializers
from .models import Board, Comment
from accounts.models import User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'board', 'parent_comment', 'content', 'created_at', 'updated_at']
        read_only_fields = ['user', 'board', 'created_at', 'updated_at']

class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)  # user의 name 필드를 user_name으로 시리얼라이즈합니다.

    
    class Meta:
        model = Board
        fields = ['id', 'user','user_name', 'title', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['user', 'created_at', 'updated_at']
