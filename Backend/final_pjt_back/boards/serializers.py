from rest_framework import serializers
from .models import Board, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'board', 'parent_comment', 'content', 'created_at', 'updated_at']
        read_only_fields = ['user', 'board', 'created_at', 'updated_at']

class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['user', 'created_at', 'updated_at']
