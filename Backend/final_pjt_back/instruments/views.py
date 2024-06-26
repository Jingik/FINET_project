from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import *
from .serializers import *
from django.db.models import Avg


## 예금
@api_view(['GET'])
def save_deposit_products(request):
    print("save_deposit_products view reached")  # Debug statement
    api_key = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    base_list = response.get('result', {}).get('baseList', [])
    option_list = response.get('result', {}).get('optionList', [])

    base_list_data = []  # Collect base list data for response
    option_list_data = []  # Collect option list data for response
    print(response)
    for item in base_list:
        if DepositProducts.objects.filter(deposit_code=item.get('fin_prdt_cd')).exists():
            continue
        item['deposit_code'] = item.pop('fin_prdt_cd')  # Change key to match the model field
        
        # Ensure all required fields are present and valid
        required_fields = ['fin_co_no', 'kor_co_nm', 'fin_prdt_nm', 'dcls_month', 'join_way', 'mtrt_int', 'spcl_cnd', 'join_deny', 'join_member', 'etc_note', 'max_limit', 'dcls_strt_day', 'dcls_end_day', 'fin_co_subm_day']
        for field in required_fields:
            if field not in item:
                item[field] = '' if isinstance(item.get(field), str) else None  # Set default value if field is missing

        serializer = DepositProductsSerializer(data=item)
        if serializer.is_valid():
            deposit_product = serializer.save()
            base_list_data.append(serializer.data)  # Add to collected base list data
        else:
            print("DepositProductsSerializer errors:", serializer.errors)  # Print errors for debugging

    for option in option_list:
        fin_prdt_cd = option.get('fin_prdt_cd')
        deposit_product = get_object_or_404(DepositProducts, deposit_code=fin_prdt_cd)
        option['deposit'] = deposit_product.id  # deposit 필드에 DepositProducts 인스턴스의 ID 할당
        option['deposit_code'] = fin_prdt_cd  # deposit_code 필드에 금융 상품 코드 할당
        
        # Ensure all required fields are present and valid
        required_fields = ['intr_rate_type_nm', 'intr_rate', 'intr_rate2', 'save_trm']
        for field in required_fields:
            if field not in option:
                option[field] = 0.0 if 'rate' in field else ''  # Set default value if field is missing

        serializer = DepositOptionsSerializer(data=option)
        if serializer.is_valid():
            deposit_option = serializer.save()
            option_list_data.append(serializer.data)
        else:
            print("DepositOptionsSerializer errors:", serializer.errors)
            
    response_data = {
        'message': 'Data saved successfully',
        'base_list_data': base_list_data,  # Include collected base list data
        'option_list_data': option_list_data,  # Include collected option list data
    }

    return JsonResponse(response_data)


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    deposit_product = get_object_or_404(DepositProducts, deposit_code=fin_prdt_cd)
    options = DepositOptions.objects.filter(deposit=deposit_product)
    serializers = DepositOptionsSerializer(options, many=True)
    return Response(serializers.data)

## 상품 Top Rate 1개 추천 
# @api_view(['GET'])
# def deposit_top_rate(request):
#     if request.method == 'GET':
#         top_rate_option = DepositOptions.objects.all().order_by('-intr_rate2').first()
#         if not top_rate_option:
#             return Response({'error': 'No deposit options found'}, status=status.HTTP_404_NOT_FOUND)
        
#         fin_prdt_cd = top_rate_option.deposit_code
#         dpst_prdt = get_object_or_404(DepositProducts, deposit_code=fin_prdt_cd)
#         dpst_prdt_serializer = DepositProductsSerializer(dpst_prdt)
#         dpst_opts = DepositOptions.objects.filter(deposit=dpst_prdt)
#         dpst_opts_serializers = DepositOptionsSerializer(dpst_opts, many=True)
        
#         response_data = {
#             "deposit_product": dpst_prdt_serializer.data,
#             "options": dpst_opts_serializers.data,
#         }
        
#         return Response(response_data)

@api_view(['GET'])
def deposit_top_rate(request):
    if request.method == 'GET':
        top_rate_options = DepositOptions.objects.all().order_by('-intr_rate2')
        if not top_rate_options:
            return Response({'error': 'No deposit options found'}, status=status.HTTP_404_NOT_FOUND)
        
        top_rate_options_serializers = DepositOptionsSerializer(top_rate_options, many=True)
        
        response_data = {
            "top_rate_options": top_rate_options_serializers.data,
        }
        
        return Response(response_data)
    
## 적금 

@api_view(['GET'])
def save_saving_products(request):
    api_key = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    base_list = response.get('result', {}).get('baseList', [])
    option_list = response.get('result', {}).get('optionList', [])

    for item in base_list:
        if SavingProducts.objects.filter(saving_code=item.get('fin_prdt_cd')).exists():
            continue
        item['saving_code'] = item.pop('fin_prdt_cd')  # Change key to match the model field
        serializer = SavingProductsSerializer(data=item)
        if serializer.is_valid():
            saving_product = serializer.save()
    
    for option in option_list:
        fin_prdt_cd = option.get('fin_prdt_cd')
        saving_product = get_object_or_404(SavingProducts, saving_code=fin_prdt_cd)
        option['saving'] = saving_product.id
        serializer = SavingOptionsSerializer(data=option)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)  # Print errors for debugging
    
    response_data = {
        'message': 'Data saved successfully',
        'base_list_data': base_list,  # Include collected base list data
        'option_list_data': option_list,  # Include collected option list data
    }

    return JsonResponse(response_data)



@api_view(['GET', 'POST'])
def saving_products(request):
    if request.method == 'GET':
        saving_products = SavingProducts.objects.all()
        serializer = SavingProductsSerializer(saving_products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SavingProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def saving_product_options(request, fin_prdt_cd):
    saving_product = get_object_or_404(SavingProducts, saving_code=fin_prdt_cd)
    options = SavingOptions.objects.filter(saving=saving_product)
    serializers = SavingOptionsSerializer(options, many=True)
    return Response(serializers.data)

# @api_view(['GET'])
# def saving_top_rate(request):
#     top_rate_option = SavingOptions.objects.all().order_by('-intr_rate2').first()
#     if not top_rate_option:
#         return Response({'error': 'No saving options found'}, status=status.HTTP_404_NOT_FOUND)
    
#     fin_prdt_cd = top_rate_option.saving.saving_code
#     svng_prdt = get_object_or_404(SavingProducts, saving_code=fin_prdt_cd)
#     svng_prdt_serializer = SavingProductsSerializer(svng_prdt)
#     svng_opts = SavingOptions.objects.filter(saving=svng_prdt)
#     svng_opts_serializers = SavingOptionsSerializer(svng_opts, many=True)
    
#     response_data = {
#         "saving_product": svng_prdt_serializer.data,
#         "options": svng_opts_serializers.data,
#     }
    
#     return Response(response_data)

@api_view(['GET'])
def saving_top_rate(request):
    if request.method == 'GET':
        top_rate_options = SavingOptions.objects.all().order_by('-intr_rate2')
        if not top_rate_options:
            return Response({'error': 'No saving options found'}, status=status.HTTP_404_NOT_FOUND)
        
        top_rate_options_serializers = SavingOptionsSerializer(top_rate_options, many=True)
        
        response_data = {
            "top_rate_options": top_rate_options_serializers.data,
        }
        
        return Response(response_data)

# 개인 신용 대출

@api_view(['GET'])
def save_creditloan_products(request):
    api_key = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    base_list = response.get('result', {}).get('baseList', [])
    option_list = response.get('result', {}).get('optionList', [])

    for item in base_list:
        if CreditLoanProducts.objects.filter(creditloan_code=item.get('fin_prdt_cd')).exists():
            continue
        item['creditloan_code'] = item.pop('fin_prdt_cd')  # Change key to match the model field
        serializer = CreditLoanProductsSerializer(data=item)
        if serializer.is_valid():
            creditloan_product = serializer.save()
    
    for option in option_list:
        fin_prdt_cd = option.get('fin_prdt_cd')
        creditloan_product = get_object_or_404(CreditLoanProducts, creditloan_code=fin_prdt_cd)
        option['creditloan'] = creditloan_product.id
        option['creditloan_code'] = fin_prdt_cd  # Change key to match the model field
        serializer = CreditLoanOptionsSerializer(data=option)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)  # Print errors for debugging
    
    response_data = {
        'message': 'Data saved successfully',
        'base_list_data': base_list,  # Include collected base list data
        'option_list_data': option_list,  # Include collected option list data
    }

    return JsonResponse(response_data)

@api_view(['GET', 'POST'])
def creditloan_products(request):
    if request.method == 'GET':
        creditloan_products = CreditLoanProducts.objects.all()
        serializer = CreditLoanProductsSerializer(creditloan_products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CreditLoanProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def creditloan_product_options(request, fin_prdt_cd):
    creditloan_product = get_object_or_404(CreditLoanProducts, creditloan_code=fin_prdt_cd)
    options = CreditLoanOptions.objects.filter(creditloan=creditloan_product)
    serializers = CreditLoanOptionsSerializer(options, many=True)
    return Response(serializers.data)

# @api_view(['GET'])
# def creditloan_top_rate(request):
#     top_rate_option = CreditLoanOptions.objects.all().order_by('-crdt_grad_1').first()
#     if not top_rate_option:
#         return Response({'error': 'No credit loan options found'}, status=status.HTTP_404_NOT_FOUND)
    
#     fin_prdt_cd = top_rate_option.creditloan.creditloan_code
#     crdtloan_prdt = get_object_or_404(CreditLoanProducts, creditloan_code=fin_prdt_cd)
#     crdtloan_prdt_serializer = CreditLoanProductsSerializer(crdtloan_prdt)
#     crdtloan_opts = CreditLoanOptions.objects.filter(creditloan=crdtloan_prdt)
#     crdtloan_opts_serializers = CreditLoanOptionsSerializer(crdtloan_opts, many=True)
    
#     response_data = {
#         "creditloan_product": crdtloan_prdt_serializer.data,
#         "options": crdtloan_opts_serializers.data,
#     }
    
#     return Response(response_data)

@api_view(['GET'])
def creditloan_top_rate(request):
    if request.method == 'GET':
        top_rate_options = CreditLoanOptions.objects.all().order_by('-crdt_grad_1')
        if not top_rate_options:
            return Response({'error': 'No credit loan options found'}, status=status.HTTP_404_NOT_FOUND)
        
        top_rate_options_serializers = CreditLoanOptionsSerializer(top_rate_options, many=True)
        
        response_data = {
            "top_rate_options": top_rate_options_serializers.data,
        }
        
        return Response(response_data)

# 상품 가입 저장
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe_deposit(request, deposit_id):
    user = request.user
    try:
        deposit_product = DepositProducts.objects.get(id=deposit_id)
        subscription, created = DepositSubscription.objects.get_or_create(user=user, deposit_product=deposit_product)
        if not created:
            return Response({'detail': '이미 가입된 상품입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = DepositSubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except DepositProducts.DoesNotExist:
        return Response({'detail': '상품을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe_saving(request, saving_id):
    user = request.user
    try:
        saving_product = SavingProducts.objects.get(id=saving_id)
        subscription, created = SavingSubscription.objects.get_or_create(user=user, saving_product=saving_product)
        if not created:
            return Response({'detail': '이미 가입된 상품입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SavingSubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except SavingProducts.DoesNotExist:
        return Response({'detail': '상품을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe_creditloan(request, creditloan_id):
    user = request.user
    try:
        creditloan_product = CreditLoanProducts.objects.get(id=creditloan_id)
        subscription, created = CreditLoanSubscription.objects.get_or_create(user=user, creditloan_product=creditloan_product)
        if not created:
            return Response({'detail': '이미 가입된 상품입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CreditLoanSubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except CreditLoanProducts.DoesNotExist:
        return Response({'detail': '상품을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
    

# 사용자가 가입한 상품 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_subscriptions(request):
    user = request.user
    
    deposit_subscriptions = DepositSubscription.objects.filter(user=user)
    saving_subscriptions = SavingSubscription.objects.filter(user=user)
    creditloan_subscriptions = CreditLoanSubscription.objects.filter(user=user)
    
    deposit_serializer = DepositSubscriptionSerializer(deposit_subscriptions, many=True)
    saving_serializer = SavingSubscriptionSerializer(saving_subscriptions, many=True)
    creditloan_serializer = CreditLoanSubscriptionSerializer(creditloan_subscriptions, many=True)
    
    return Response({
        'deposit_subscriptions': deposit_serializer.data,
        'saving_subscriptions': saving_serializer.data,
        'creditloan_subscriptions': creditloan_serializer.data,
    }, status=status.HTTP_200_OK)
    
    
    
## 찜한 상품 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_favorites(request):
    user = request.user
    deposit_favorites = FavoriteDepositProduct.objects.filter(user=user)
    saving_favorites = FavoriteSavingProduct.objects.filter(user=user)
    creditloan_favorites = FavoriteCreditLoanProduct.objects.filter(user=user)
    
    deposit_serializer = FavoriteDepositProductSerializer(deposit_favorites, many=True)
    saving_serializer = FavoriteSavingProductSerializer(saving_favorites, many=True)
    creditloan_serializer = FavoriteCreditLoanProductSerializer(creditloan_favorites, many=True)
    
    return Response({
        'deposit_subscriptions': deposit_serializer.data,
        'saving_subscriptions': saving_serializer.data,
        'creditloan_subscriptions': creditloan_serializer.data,
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorites_deposit(request):
    user = request.user
    deposit_product_id = request.data.get('deposit_product_id')
    if not deposit_product_id:
        return Response({'error': 'Deposit product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        deposit_product = DepositProducts.objects.get(id=deposit_product_id)
    except DepositProducts.DoesNotExist:
        return Response({'error': 'Deposit product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    favorite, created = FavoriteDepositProduct.objects.get_or_create(user=user, deposit_product=deposit_product)
    if created:
        return Response({'status': 'added to favorites'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status': 'already in favorites'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_favorites_deposit(request):
    user = request.user
    deposit_product_id = request.data.get('deposit_product_id')
    if not deposit_product_id:
        return Response({'error': 'Deposit product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        deposit_product = DepositProducts.objects.get(id=deposit_product_id)
    except DepositProducts.DoesNotExist:
        return Response({'error': 'Deposit product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    favorite = FavoriteDepositProduct.objects.filter(user=user, deposit_product=deposit_product)
    if favorite.exists():
        favorite.delete()
        return Response({'status': 'removed from favorites'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Favorite not found'}, status=status.HTTP_404_NOT_FOUND)

# Saving
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorites_saving(request):
    user = request.user
    saving_product_id = request.data.get('saving_product_id')
    if not saving_product_id:
        return Response({'error': 'Saving product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        saving_product = SavingProducts.objects.get(id=saving_product_id)
    except SavingProducts.DoesNotExist:
        return Response({'error': 'Saving product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    favorite, created = FavoriteSavingProduct.objects.get_or_create(user=user, saving_product=saving_product)
    if created:
        return Response({'status': 'added to favorites'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status': 'already in favorites'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_favorites_saving(request):
    user = request.user
    saving_product_id = request.data.get('saving_product_id')
    if not saving_product_id:
        return Response({'error': 'Saving product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        saving_product = SavingProducts.objects.get(id=saving_product_id)
    except SavingProducts.DoesNotExist:
        return Response({'error': 'Saving product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    favorite = FavoriteSavingProduct.objects.filter(user=user, saving_product=saving_product)
    if favorite.exists():
        favorite.delete()
        return Response({'status': 'removed from favorites'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Favorite not found'}, status=status.HTTP_404_NOT_FOUND)


#creditLoan

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorites_creditloan(request):
    user = request.user
    creditloan_product_id = request.data.get('creditloan_product_id')
    if not creditloan_product_id:
        return Response({'error': 'Creditloan product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        creditloan_product = CreditLoanProducts.objects.get(id=creditloan_product_id)
    except creditloan_product.DoesNotExist:
        return Response({'error': 'Creditloan product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    favorite, created = FavoriteCreditLoanProduct.objects.get_or_create(user=user, creditloan_product=creditloan_product)
    if created:
        return Response({'status': 'added to favorites'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status': 'already in favorites'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_favorites_creditloan(request):
    user = request.user
    creditloan_product_id = request.data.get('creditloan_product_id')
    if not creditloan_product_id:
        return Response({'error': 'Creditloan product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        creditloan_product = CreditLoanProducts.objects.get(id=creditloan_product_id)
    except CreditLoanProducts.DoesNotExist:
        return Response({'error': 'Deposit product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    favorite = FavoriteCreditLoanProduct.objects.filter(user=user, creditloan_product=creditloan_product)
    if favorite.exists():
        favorite.delete()
        return Response({'status': 'removed from favorites'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Favorite not found'}, status=status.HTTP_404_NOT_FOUND)
    

### 상품 추천
## Rating 값 계산
def calculate_saving_deposit_score(user, product):
    age_weight = 1.0
    asset_weight = 0.5
    favorites_weight = 2.0

    # 연령대 가중치
    if user['user_age_group'] == '20대':
        age_weight = 1.2
    elif user['user_age_group'] == '30대':
        age_weight = 1.5
    elif user['user_age_group'] == '40대':
        age_weight = 1.8
    elif user['user_age_group'] == '50대':
        age_weight = 2.0

    # 자산 가중치
    if user['asset'] > 100000000:
        asset_weight = 2.0
    elif user['asset'] > 50000000:
        asset_weight = 1.5

    # 찜한 상품 가중치
    favorites_count = FavoriteDepositProduct.objects.filter(deposit_product=product).count() if isinstance(product, DepositProducts) else FavoriteSavingProduct.objects.filter(saving_product=product).count()

    return age_weight * asset_weight * (1 + favorites_weight * favorites_count)

def calculate_creditloan_score(user, product):
    age_weight = 1.0
    asset_weight = 0.5
    limit_weight = 1.5
    favorites_weight = 2.0

    # 연령대 가중치
    if user['user_age_group'] == '20대':
        age_weight = 0.4
    elif user['user_age_group'] == '30대':
        age_weight = 1.0
    elif user['user_age_group'] == '40대':
        age_weight = 1.5
    elif user['user_age_group'] == '50대':
        age_weight = 2.0

    # 자산 가중치
    if user['asset'] > 100000000:
        asset_weight = 2.0
    elif user['asset'] > 50000000:
        asset_weight = 1.5
    elif user['asset'] > 25000000:
        asset_weight = 1.0
    elif user['asset'] > 10000000:
        asset_weight = 0.5

    # 최대 한도 가중치
    limit_score = product.max_limit / 1000000 if product.max_limit else 1

    # 찜한 상품 가중치
    favorites_count = FavoriteCreditLoanProduct.objects.filter(creditloan_product=product).count()

    return age_weight * asset_weight * limit_weight * limit_score * (1 + favorites_weight * favorites_count)

def recommend_products(user):
    # 예금 상품 추천
    deposit_products = DepositProducts.objects.all()
    deposit_scores = [(product, calculate_saving_deposit_score(user, product)) for product in deposit_products]
    deposit_recommendations = sorted(deposit_scores, key=lambda x: x[1], reverse=True)[:5]

    # 적금 상품 추천
    saving_products = SavingProducts.objects.all()
    saving_scores = [(product, calculate_saving_deposit_score(user, product)) for product in saving_products]
    saving_recommendations = sorted(saving_scores, key=lambda x: x[1], reverse=True)[:5]

    # 신용 대출 상품 추천
    creditloan_products = CreditLoanProducts.objects.all()
    creditloan_scores = [(product, calculate_creditloan_score(user, product)) for product in creditloan_products]
    creditloan_recommendations = sorted(creditloan_scores, key=lambda x: x[1], reverse=True)[:5]

    return deposit_recommendations, saving_recommendations, creditloan_recommendations

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recommend_view_rating(request):
    user_data = request.data
    if 'user_age_group' not in user_data or 'asset' not in user_data:
        return Response({"error": "User profile data is incomplete"}, status=status.HTTP_400_BAD_REQUEST)

    deposit_recommendations, saving_recommendations, creditloan_recommendations = recommend_products(user_data)

    context = {
        'deposit_recommendations': DepositProductsSerializer([rec[0] for rec in deposit_recommendations], many=True).data,
        'saving_recommendations': SavingProductsSerializer([rec[0] for rec in saving_recommendations], many=True).data,
        'creditloan_recommendations': CreditLoanProductsSerializer([rec[0] for rec in creditloan_recommendations], many=True).data,
    }

    return Response(context, status=status.HTTP_200_OK)


## 가장 많이 담은 순
def recommend_products_count(user):
    # Recommend deposit products favored by users in the same age group
    deposit_recommendations = DepositProducts.objects.filter(
        favoritedepositproduct__user__user_age_group=user.user_age_group
    ).annotate(num_users=Count('favoritedepositproduct')).order_by('-num_users')[:5]

    # Recommend saving products favored by users in the same age group
    saving_recommendations = SavingProducts.objects.filter(
        favoritesavingproduct__user__user_age_group=user.user_age_group
    ).annotate(num_users=Count('favoritesavingproduct')).order_by('-num_users')[:5]

    # Recommend credit loan products favored by users in the same age group
    creditloan_recommendations = CreditLoanProducts.objects.filter(
        favoritecreditloanproduct__user__user_age_group=user.user_age_group
    ).annotate(num_users=Count('favoritecreditloanproduct')).order_by('-num_users')[:5]

    return deposit_recommendations, saving_recommendations, creditloan_recommendations


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_view_counting(request):
    user = request.user
    deposit_recommendations, saving_recommendations, creditloan_recommendations = recommend_products_count(user)
    
    deposit_serializer = DepositProductsSerializer(deposit_recommendations, many=True)
    saving_serializer = SavingProductsSerializer(saving_recommendations, many=True)
    creditloan_serializer = CreditLoanProductsSerializer(creditloan_recommendations, many=True)

    response_data = {
        'deposit_recommendations': deposit_serializer.data,
        'saving_recommendations': saving_serializer.data,
        'creditloan_recommendations': creditloan_serializer.data
    }
    return Response(response_data, status=status.HTTP_200_OK)





## Dot production

def vectorize_user(user):
    # 사용자 정보를 벡터화하는 예시
    age_group_vector = {
        '10대': 0.1,
        '20대': 0.2,
        '30대': 0.3,
        '40대': 0.4,
        '50대': 0.5
    }
    service_purpose_vector = {
        '예금 가입': 0.1,
        '적금 가입': 0.2,
        '대출 가입': 0.3
    }
    vector = [
        user['asset'],
        age_group_vector.get(user['user_age_group'], 0),
        service_purpose_vector.get(user['service_purpose'], 0),
    ]
    return vector

def vectorize_product(product):
    if isinstance(product, DepositProducts):
        vector = [
            product.max_limit if product.max_limit else 0,
            max([option.intr_rate for option in product.depositoptions_set.all() if option.intr_rate is not None] if hasattr(product, 'depositoptions_set') else [0]),
            product.join_deny if product.join_deny is not None else 0,
            len(product.join_member) if product.join_member else 0,
            int(product.dcls_month) if product.dcls_month else 0,
            len(product.join_way) if product.join_way else 0,
            len(product.spcl_cnd) if product.spcl_cnd else 0,
        ]
    elif isinstance(product, SavingProducts):
        vector = [
            product.max_limit if product.max_limit else 0,
            max([option.intr_rate for option in product.savingoptions_set.all() if option.intr_rate is not None] if hasattr(product, 'savingoptions_set') else [0]),
            product.join_deny if product.join_deny is not None else 0,
            len(product.join_member) if product.join_member else 0,
            int(product.dcls_month) if product.dcls_month else 0,
            len(product.join_way) if product.join_way else 0,
            len(product.spcl_cnd) if product.spcl_cnd else 0,
        ]
    elif isinstance(product, CreditLoanProducts):
        vector = [
            product.max_limit if product.max_limit else 0,
            product.creditloanoptions_set.aggregate(Avg('crdt_grad_avg'))['crdt_grad_avg__avg'] if product.creditloanoptions_set.exists() else 0,
            len(product.join_way) if product.join_way else 0,
            len(product.spcl_cnd) if product.spcl_cnd else 0,
        ]
    return vector


def dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))

def calculate_recommendation_score(user, product):
    user_vector = vectorize_user(user)
    product_vector = vectorize_product(product)
    return dot_product(user_vector, product_vector)

def recommend_products_dot(user):
    # 예금 상품 추천
    deposit_products = DepositProducts.objects.all()
    deposit_scores = [(product, calculate_recommendation_score(user, product)) for product in deposit_products]
    deposit_recommendations = sorted(deposit_scores, key=lambda x: x[1], reverse=True)[:5]

    # 적금 상품 추천
    saving_products = SavingProducts.objects.all()
    saving_scores = [(product, calculate_recommendation_score(user, product)) for product in saving_products]
    saving_recommendations = sorted(saving_scores, key=lambda x: x[1], reverse=True)[:5]

    # 신용 대출 상품 추천
    creditloan_products = CreditLoanProducts.objects.all()
    creditloan_scores = [(product, calculate_recommendation_score(user, product)) for product in creditloan_products]
    creditloan_recommendations = sorted(creditloan_scores, key=lambda x: x[1], reverse=True)[:5]

    return deposit_recommendations, saving_recommendations, creditloan_recommendations

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recommend_view_dot(request):
    user_data = request.data
    if 'user_age_group' not in user_data or 'asset' not in user_data or 'service_purpose' not in user_data:
        return Response({"error": "User profile data is incomplete"}, status=status.HTTP_400_BAD_REQUEST)

    deposit_recommendations, saving_recommendations, creditloan_recommendations = recommend_products_dot(user_data)

    context = {
        'deposit_recommendations': DepositProductsSerializer([rec[0] for rec in deposit_recommendations], many=True).data,
        'saving_recommendations': SavingProductsSerializer([rec[0] for rec in saving_recommendations], many=True).data,
        'creditloan_recommendations': CreditLoanProductsSerializer([rec[0] for rec in creditloan_recommendations], many=True).data,
    }

    return Response(context, status=status.HTTP_200_OK)
