from django.urls import path
from . import views

urlpatterns = [
    # 예금
    path('save-deposit-products/', views.save_deposit_products, name="save_deposit_products"),
    path('deposit-products/', views.deposit_products, name="deposit_products"),
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_product_options, name="deposit_product_options"),
    path('deposit-products/top_rate/', views.deposit_top_rate, name="top_rate"),
    
    # 적금 
    path('save-saving-products/', views.save_saving_products, name='save_saving_products'),
    path('saving-products/', views.saving_products, name='saving_products'),
    path('saving-product-options/<str:fin_prdt_cd>/', views.saving_product_options, name='saving_product_options'),
    path('saving-top-rate/', views.saving_top_rate, name='saving_top_rate'),
    
    # 개인 신용 대출
    path('save-creditloan-products/', views.save_creditloan_products, name='save_creditloan_products'),
    path('creditloan-products/', views.creditloan_products, name='creditloan_products'),
    path('creditloan-product-options/<str:fin_prdt_cd>/', views.creditloan_product_options, name='creditloan_product_options'),
    path('creditloan-top-rate/', views.creditloan_top_rate, name='creditloan_top_rate'),
]
