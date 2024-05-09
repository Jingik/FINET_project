from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
import requests
from rest_framework import status
from django.conf import settings
from rest_framework.response import Response


## 예금
## fin_prdt_cd 바꿔야됨 다 
@api_view(['GET'])
def save_deposit_products(request):
    api_key = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    base_list = response.get('result', {}).get('baseList', [])
    option_list = response.get('result', {}).get('optionList', [])

    for item in base_list:
        
        if DepositProducts.objects.filter(fin_prdt_cd=item.get('fin_prdt_cd')).exists() :
            continue
        serializer = DepositProductsSerializer(data=item)
        if serializer.is_valid():
            deposit_product = serializer.save()
    
    # Save deposit options
    for option in option_list:
        fin_prdt_cd = option.get('fin_prdt_cd')
        deposit_product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        
        serializer = DepositOptionsSerializer(data=option)
        if serializer.is_valid():
            serializer.save(product=deposit_product)
    
    return JsonResponse({'message': 'Data saved successfully'})



@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializers = DepositOptionsSerializer(options, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def deposit_top_rate(request):
    if request.method == 'GET':
        # 금리가 가장 높은 옵션 선택
        top_rate_option = DepositOptions.objects.all().order_by('-intr_rate2')[0]
        # 금융 상품 코드 추출
        fin_prdt_cd = top_rate_option.fin_prdt_cd
        
        # 해당 코드로 금융 상품 검색
        dpst_prdt = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        dpst_prdt_serializer = DepositProductsSerializer(dpst_prdt)
        # 옵션 리스트 검색
        dpst_opts = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
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
        
        if SavingProducts.objects.filter(fin_prdt_cd=item.get('fin_prdt_cd')).exists() :
            continue
        serializer = SavingProductsSerializer(data=item)
        if serializer.is_valid():
            saving_product = serializer.save()
    
    # Save saving options
    for option in option_list:
        fin_prdt_cd = option.get('fin_prdt_cd')
        Saving_product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        
        serializer = SavingOptionsSerializer(data=option)
        if serializer.is_valid():
            serializer.save(product=Saving_product)
    
    return JsonResponse({'message': 'Data saved successfully'})



@api_view(['GET', 'POST'])
def saving_products(request):
    if request.method == 'GET':
        saving_products = SavingProducts.objects.all()
        serializer = SavingProductsSerializer(saving_products, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SavingProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def saving_product_options(request, fin_prdt_cd):
    options = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializers = SavingOptionsSerializer(options, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def saving_top_rate(request):
    if request.method == 'GET':
        # 금리가 가장 높은 옵션 선택
        top_rate_option = SavingOptions.objects.all().order_by('-intr_rate2')[0]
        # 금융 상품 코드 추출
        fin_prdt_cd = top_rate_option.fin_prdt_cd
        
        # 해당 코드로 금융 상품 검색
        dpst_prdt = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        dpst_prdt_serializer = SavingProductsSerializer(dpst_prdt)
        # 옵션 리스트 검색
        dpst_opts = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        dpst_opts_serializers = SavingOptionsSerializer(dpst_opts, many=True)
        
        response_data = {
            "saving_product": dpst_prdt_serializer.data,
            "options": dpst_opts_serializers.data,
        }
        
        return Response(response_data)


## 개인 신용 대출
## 모델도 아직 안 만듬
## serializer도 아직 안 만듬
@api_view(['GET'])
def save_creditLoan_products(request):
    api_key = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    base_list = response.get('result', {}).get('baseList', [])
    option_list = response.get('result', {}).get('optionList', [])

    for item in base_list:
        
        if DepositProducts.objects.filter(fin_prdt_cd=item.get('fin_prdt_cd')).exists() :
            continue
        serializer = DepositProductsSerializer(data=item)
        if serializer.is_valid():
            deposit_product = serializer.save()
    
    # Save deposit options
    for option in option_list:
        fin_prdt_cd = option.get('fin_prdt_cd')
        deposit_product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        
        serializer = DepositOptionsSerializer(data=option)
        if serializer.is_valid():
            serializer.save(product=deposit_product)
    
    return JsonResponse({'message': 'Data saved successfully'})



@api_view(['GET', 'POST'])
def creditLoan_products(request):
    if request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def creditLoan_product_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializers = DepositOptionsSerializer(options, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def creditLoan_top_rate(request):
    if request.method == 'GET':
        # 금리가 가장 높은 옵션 선택
        top_rate_option = DepositOptions.objects.all().order_by('-intr_rate2')[0]
        # 금융 상품 코드 추출
        fin_prdt_cd = top_rate_option.fin_prdt_cd
        
        # 해당 코드로 금융 상품 검색
        dpst_prdt = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        dpst_prdt_serializer = DepositProductsSerializer(dpst_prdt)
        # 옵션 리스트 검색
        dpst_opts = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        dpst_opts_serializers = DepositOptionsSerializer(dpst_opts, many=True)
        
        response_data = {
            "deposit_product": dpst_prdt_serializer.data,
            "options": dpst_opts_serializers.data,
        }
        
        return Response(response_data)