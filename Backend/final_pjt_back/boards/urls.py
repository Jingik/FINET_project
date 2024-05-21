from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),  # 게시판 목록 조회 및 게시글 생성
    path('<int:pk>/', views.board_detail, name='board_detail'),  # 게시글 상세 조회, 수정, 삭제
    path('create/', views.create_board, name='create_board'),  # 게시글 생성
    path('<int:pk>/update/', views.update_board, name='update_board'),  # 게시글 수정

    # 댓글 관련 경로
    path('<int:board_id>/comments/', views.comment_list, name='comment_list'),  # 댓글 목록 조회 및 댓글 생성
    path('<int:board_id>/comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),  # 댓글 수정 및 삭제

    # 사용자가 작성한 게시글 및 댓글 조회
    path('user/boards/', views.user_boards, name='user_boards'),  
    path('user/comments/', views.user_comments, name='user_comments'),
    
    # 사용자가 좋아요 누른 글 및 댓글 확인하기
    path('like_board/<int:board_id>/', views.like_board, name='like_board'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'), 
    path('liked_content/', views.liked_content, name='liked_content'),
]
