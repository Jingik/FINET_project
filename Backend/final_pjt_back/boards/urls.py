from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('<int:pk>/', views.board_detail, name='board_detail'),
    path('<int:board_id>/comments/', views.comment_list, name='comment_list'),
    path('<int:board_id>/comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('user/boards/', views.user_boards, name='user_boards'),  
    path('user/comments/', views.user_comments, name='user_comments'), 
    path('create/', views.create_board, name='create_board'),
]
