"""
URL configuration for final_pjt_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='board_create'),
    path('<int:pk>/', views.detail, name='board_detail'),
    path('<int:pk>/update/', views.update, name='board_update'),
    path('<int:pk>/delete/', views.delete, name='board_delete'), # Assuming you want a delete endpoint for the board
    path('<int:pk>/comments/', views.comments_create, name='comments_create'), # Changed from 'comment' to 'comments_create'
    # path('<int:pk>/comments/<int:comment_pk>/', views.comments_detail, name='comment_detail'), # Assuming you want a detail view for comments
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]


