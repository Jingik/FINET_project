from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import *
from .serializers import *

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

@api_view(['GET'])
def deposit_top_rate(request):
    if request.method == 'GET':
        top_rate_option = DepositOptions.objects.all().order_by('-intr_rate2').first()
        if not top_rate_option:
            return Response({'error': 'No deposit options found'}, status=status.HTTP_404_NOT_FOUND)
        
        fin_prdt_cd = top_rate_option.deposit_code
        dpst_prdt = get_object_or_404(DepositProducts, deposit_code=fin_prdt_cd)
        dpst_prdt_serializer = DepositProductsSerializer(dpst_prdt)
        dpst_opts = DepositOptions.objects.filter(deposit=dpst_prdt)
        dpst_opts_serializers = DepositOptionsSerializer(dpst_opts, many=True)
        
        response_data = {
            "deposit_product": dpst_prdt_serializer.data,
            "options": dpst_opts_serializers.data,
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

@api_view(['GET'])
def saving_top_rate(request):
    top_rate_option = SavingOptions.objects.all().order_by('-intr_rate2').first()
    if not top_rate_option:
        return Response({'error': 'No saving options found'}, status=status.HTTP_404_NOT_FOUND)
    
    fin_prdt_cd = top_rate_option.saving.saving_code
    svng_prdt = get_object_or_404(SavingProducts, saving_code=fin_prdt_cd)
    svng_prdt_serializer = SavingProductsSerializer(svng_prdt)
    svng_opts = SavingOptions.objects.filter(saving=svng_prdt)
    svng_opts_serializers = SavingOptionsSerializer(svng_opts, many=True)
    
    response_data = {
        "saving_product": svng_prdt_serializer.data,
        "options": svng_opts_serializers.data,
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

@api_view(['GET'])
def creditloan_top_rate(request):
    top_rate_option = CreditLoanOptions.objects.all().order_by('-crdt_grad_1').first()
    if not top_rate_option:
        return Response({'error': 'No credit loan options found'}, status=status.HTTP_404_NOT_FOUND)
    
    fin_prdt_cd = top_rate_option.creditloan.creditloan_code
    crdtloan_prdt = get_object_or_404(CreditLoanProducts, creditloan_code=fin_prdt_cd)
    crdtloan_prdt_serializer = CreditLoanProductsSerializer(crdtloan_prdt)
    crdtloan_opts = CreditLoanOptions.objects.filter(creditloan=crdtloan_prdt)
    crdtloan_opts_serializers = CreditLoanOptionsSerializer(crdtloan_opts, many=True)
    
    response_data = {
        "creditloan_product": crdtloan_prdt_serializer.data,
        "options": crdtloan_opts_serializers.data,
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
            return Response({'detail': 'Already subscribed'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = DepositSubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except DepositProducts.DoesNotExist:
        return Response({'detail': 'Deposit product not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe_saving(request, saving_id):
    user = request.user
    try:
        saving_product = SavingProducts.objects.get(id=saving_id)
        subscription, created = SavingSubscription.objects.get_or_create(user=user, saving_product=saving_product)
        if not created:
            return Response({'detail': 'Already subscribed'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SavingSubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except SavingProducts.DoesNotExist:
        return Response({'detail': 'Saving product not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe_creditloan(request, creditloan_id):
    user = request.user
    try:
        creditloan_product = CreditLoanProducts.objects.get(id=creditloan_id)
        subscription, created = CreditLoanSubscription.objects.get_or_create(user=user, creditloan_product=creditloan_product)
        if not created:
            return Response({'detail': 'Already subscribed'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CreditLoanSubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except CreditLoanProducts.DoesNotExist:
        return Response({'detail': 'Credit loan product not found'}, status=status.HTTP_404_NOT_FOUND)
    

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