from django.urls import path
from . import views

urlpatterns = [
    # 예금
    path('save-deposit-products/', views.save_deposit_products, name="save_deposit_products"),
    path('deposit-products/', views.deposit_products, name="deposit_products"),
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_product_options, name="deposit_product_options"),
    
    # 적금 
    path('save-saving-products/', views.save_saving_products, name='save_saving_products'),
    path('saving-products/', views.saving_products, name='saving_products'),
    path('saving-product-options/<str:fin_prdt_cd>/', views.saving_product_options, name='saving_product_options'),
    
    # 개인 신용 대출
    path('save-creditloan-products/', views.save_creditloan_products, name='save_creditloan_products'),
    path('creditloan-products/', views.creditloan_products, name='creditloan_products'),
    path('creditloan-product-options/<str:fin_prdt_cd>/', views.creditloan_product_options, name='creditloan_product_options'),
    
    # 상품 가입 저장
    path('subscribe_deposit/<int:deposit_id>/', views.subscribe_deposit, name='subscribe_deposit'),
    path('subscribe_saving/<int:saving_id>/', views.subscribe_saving, name='subscribe_saving'),
    path('subscribe_creditloan/<int:creditloan_id>/', views.subscribe_creditloan, name='subscribe_creditloan'),
    
    # 가입 상품 조회
    path('user_subscriptions/', views.user_subscriptions, name='user_subscriptions'),
    
    # 찜한 상품 저장
    path('favorites/add_deposit/', views.add_favorites_deposit, name='add_favorites_deposit'),
    path('favorites/add_saving/', views.add_favorites_saving, name='add_favorites_saving'),
    path('favorites/add_creditloan/', views.add_favorites_creditloan, name='add_favorites_creditloan'),
    
    # 찜한 상품 삭제 
    path('favorites/remove_deposit/', views.remove_favorites_deposit, name='remove_favorites_deposit'),
    path('favorites/remove_saving/', views.remove_favorites_saving, name='remove_favorites_saving'),
    path('favorites/remove_creditloan/', views.remove_favorites_creditloan, name='remove_favorites_creditloan'),
    
    # 찜한 상품 조회
    path('favorites/', views.list_favorites, name='list_favorites'),
    
    # 상품 추천
    ## 금리 순 (대출은 낮고, 예적금은 높은 순)
    path('deposit-products/top_rate/', views.deposit_top_rate, name="top_rate"),
    path('saving-top-rate/', views.saving_top_rate, name='saving_top_rate'),
    path('creditloan-top-rate/', views.creditloan_top_rate, name='creditloan_top_rate'),
    ## Rating 값 계산
    path('recommend_rating/', views.recommend_view_rating, name='recommend_view_rating'),
    ## 많이 담은 순
    path('recommend_count/', views.recommend_view_counting, name='recommend_view_counting'),
    ## dot_production
    path('recommend_dot/', views.recommend_view_dot, name='recommend_view_dot'),
    
    
]
