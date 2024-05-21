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
    path('signup/', views.signup, name='signup'),
    path('me/', views.current_user, name='me'),
    path('id_check_exists/', views.id_check_exists, name='id_check_exists'),
    path('login/', views.user_login, name='user_login'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('subscribe_product/', views.subscribe_product, name='subscribe_product'),
    path('user_subscriptions/', views.user_subscriptions, name='user_subscriptions'),
]
