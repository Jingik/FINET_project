from django.urls import path
from . import views

urlpatterns = [
    path('boards/', views.board_list, name='board_list'),
    path('boards/<int:pk>/', views.board_detail, name='board_detail'),
    path('boards/<int:board_id>/comments/', views.comment_list, name='comment_list'),
    path('boards/<int:board_id>/comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('user/boards/', views.user_boards, name='user_boards'),  
    path('user/comments/', views.user_comments, name='user_comments'), 
]
