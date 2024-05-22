from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def board_list(request):
    if request.method == 'GET':
        boards = Board.objects.all().order_by('-created_at')
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(boards, request)
        serializer = BoardSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_board(request):
    data = JSONParser().parse(request)
    serializer = BoardSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'GET':
        serializer = BoardSerializer(board)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(board, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_list(request, board_id):
    board = get_object_or_404(Board, pk=board_id)

    if request.method == 'GET':
        comments = Comment.objects.filter(board=board, parent_comment__isnull=True).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user, board=board)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, board_id, comment_id):
    board = get_object_or_404(Board, pk=board_id)
    comment = get_object_or_404(Comment, pk=comment_id, board=board)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_boards(request):
    boards = Board.objects.filter(user=request.user).order_by('-created_at')
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(boards, request)
    serializer = BoardSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_comments(request):
    comments = Comment.objects.filter(user=request.user).order_by('-created_at')
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(comments, request)
    serializer = CommentSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_board(request, pk):
    board = get_object_or_404(Board, pk=pk)
    data = JSONParser().parse(request)
    serializer = BoardSerializer(board, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_board(request, board_id):
    user = request.user
    try:
        board = Board.objects.get(id=board_id)
        like, created = BoardLike.objects.get_or_create(user=user, board=board)
        if not created:
            return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = BoardLikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Board.DoesNotExist:
        return Response({'detail': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_board(request, board_id):
    user = request.user
    try:
        board = Board.objects.get(id=board_id)
        like = BoardLike.objects.filter(user=user, board=board).first()
        if like:
            like.delete()
            return Response({'detail': 'Unliked'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'Not liked yet'}, status=status.HTTP_400_BAD_REQUEST)
    except Board.DoesNotExist:
        return Response({'detail': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_comment(request, comment_id):
    user = request.user
    print(f"Received request to like comment with ID: {comment_id} from user: {user.id}")
    try:
        comment = Comment.objects.get(id=comment_id)
        print(f"Found comment with ID: {comment_id}")
        like, created = CommentLike.objects.get_or_create(user=user, comment=comment)
        if not created:
            print("Comment already liked by this user.")
            return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CommentLikeSerializer(like)
        print("Comment liked successfully.")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Comment.DoesNotExist:
        print("Comment not found.")
        return Response({'detail': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
    except ValidationError as ve:
        print(f"Validation error: {ve}")
        return Response({'detail': str(ve)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return Response({'detail': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_comment(request, comment_id):
    user = request.user
    try:
        comment = Comment.objects.get(id=comment_id)
        like = CommentLike.objects.filter(user=user, comment=comment).first()
        if like:
            like.delete()
            return Response({'detail': 'Unliked'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'Not liked yet'}, status=status.HTTP_400_BAD_REQUEST)
    except Comment.DoesNotExist:
        return Response({'detail': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liked_content(request):
    user = request.user
    liked_boards = Board.objects.filter(boardlike__user=user)
    liked_comments = Comment.objects.filter(commentlike__user=user)
    
    board_serializer = BoardSerializer(liked_boards, many=True)
    comment_serializer = CommentSerializer(liked_comments, many=True)
    
    return Response({
        'liked_boards': board_serializer.data,
        'liked_comments': comment_serializer.data,
    }, status=status.HTTP_200_OK)