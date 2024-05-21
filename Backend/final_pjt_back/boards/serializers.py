from rest_framework import serializers
from .models import Board, Comment, BoardLike, CommentLike
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'phone_number', 'email', 'user_age_group', 'service_purpose', 'asset']

class BoardLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardLike
        fields = ['user', 'board', 'liked_at']

class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['user', 'comment', 'liked_at']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_name', 'user_id', 'board', 'parent_comment', 'content', 'created_at', 'updated_at', 'likes_count']
        read_only_fields = ['user', 'board', 'created_at', 'updated_at']

    def get_likes_count(self, obj):
        return obj.commentlike_set.count()

class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ['id', 'user', 'user_name', 'title', 'content', 'created_at', 'updated_at', 'comments', 'likes_count']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def get_likes_count(self, obj):
        return obj.boardlike_set.count()
