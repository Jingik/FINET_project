from django.urls import path
from . import views

app_name="instruments"
urlpatterns = [
    # 예금
    path('save-deposit-products/', views.save_deposit_products, name="save_deposit_products"),
    path('deposit-products/', views.deposit_products, name="deposit_products"),
    path('deposit-products-options/<str:fin_prdt_cd>', views.deposit_product_options, name="deposit_product_options"),
    path('deposit-products/top_rate/', views.deposit_top_rate , name="top_rate "),
    
    # 적금    
    path('save-saving-products/', views.save_saving_products, name="save_saving_products"),
    path('saving-products/', views.saving_products, name="saving_products"),
    path('saving-products-options/<str:fin_prdt_cd>', views.saving_product_options, name="saving_product_options"),
    path('saving-products/top_rate/', views.saving_top_rate , name="saving_top_rate "),
    
    # 대출
    path('save-creditLoan-products/', views.save_creditLoan_products, name="save_creditLoan_products"),
    path('creditLoan-products/', views.creditLoan_products, name="creditLoan_products"),
    path('creditLoan-products-options/<str:fin_prdt_cd>', views.creditLoan_product_options, name="creditLoan_product_options"),
    path('creditLoan-products/top_rate/', views.creditLoan_top_rate , name="creditLoan_top_rate "),
]
