from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Board, Comment
from .serializers import BoardSerializer, CommentSerializer
from django.shortcuts import get_object_or_404

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def board_list(request):
#     if request.method == 'GET':
#         boards = Board.objects.all().order_by('-created_at')
#         paginator = PageNumberPagination()
#         paginator.page_size = 10
#         result_page = paginator.paginate_queryset(boards, request)
#         serializer = BoardSerializer(result_page, many=True)
#         return paginator.get_paginated_response(serializer.data)

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

# 본인이 작성한 게시글 및 댓글
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
