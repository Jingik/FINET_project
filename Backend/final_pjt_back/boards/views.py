from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Board, Comment
from .serializers import BoardSerializer, CommentSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from io import BytesIO

## 애매하게 view 구현

@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        return Response({'message': 'The board does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        comments = board.comment_set.all()
        board_serializer = BoardSerializer(board)
        comments_serializer = CommentSerializer(comments, many=True)
        return Response({
            'board': board_serializer.data,
            'comments': comments_serializer.data
        })

@method_decorator(login_required, name='dispatch')
@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(login_required, name='dispatch')
@api_view(['PUT', 'GET'])
def update(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        return Response({'message': 'The board does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.user != board.user:
        return Response({'message': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = BoardSerializer(board)
        return

@method_decorator(login_required, name='dispatch')
@api_view(['DELETE'])
def delete(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        return Response({'message': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.user != board.user:
        return Response({'message': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'DELETE':
        board.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@method_decorator(login_required, name='dispatch')
@api_view(['POST'])
def comments_create(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        return Response({'message': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, board=board)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(login_required, name='dispatch')
@api_view(['DELETE'])
def comments_delete(request, board_pk, comment_pk):
    try:
        comment = Comment.objects.get(pk=comment_pk)
    except Comment.DoesNotExist:
        return Response({'message': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.user != comment.user:
        return Response({'message': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'DELETE':
        comment.delete()
        return Response({'message': 'Comment deleted'}, status=status.HTTP_204_NO_CONTENT)