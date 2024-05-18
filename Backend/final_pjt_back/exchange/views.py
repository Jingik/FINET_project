from django.conf import settings
from rest_framework.response import Response
from .models import Exchange
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from .serializers import ExchangeSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


# EXCHANGE_API_KEY = 'BDEnNlZa0E5gjifaBugXl6cHON5XSFnZ' # 환율 API 키
EXCHANGE_API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={settings.EXCHANGE_API_KEY}&data=AP01'

@api_view(['GET'])
def index(request):
    """
    외부 API로부터 환율 데이터를 가져와서 로컬 데이터베이스를 업데이트하는 함수.
    - 외부 API가 데이터를 반환하면, 해당 데이터로 로컬 Exchange 테이블을 업데이트.
    - 외부 API가 데이터를 반환하지 않으면, 현재 로컬 Exchange 테이블의 데이터를 반환.
    """
    # 외부 API로부터 환율 데이터 가져오기
    response = requests.get(EXCHANGE_API_URL).json()
    exchange_response = Exchange.objects.all()
   
    if response: 
        # 외부 API 응답이 있을 경우
        if not exchange_response: 
            # 로컬 데이터베이스에 기존 데이터가 없을 경우
            serializer = ExchangeSerializer(data=response, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else: 
            # 로컬 데이터베이스에 기존 데이터가 있을 경우, 모든 데이터를 삭제하고 새 데이터 저장
            Exchange.objects.all().delete()
            serializer = ExchangeSerializer(data=response, many=True)     
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    
    # 외부 API 응답이 없을 경우, 로컬 데이터베이스의 기존 데이터 반환
    serializer = ExchangeSerializer(exchange_response, many=True)
    return Response(serializer.data)

def exchange_rate_detail(request, cur_unit):
    try:
        exchange_rate = Exchange.objects.get(cur_unit=cur_unit)
        data = {
            'cur_unit': exchange_rate.cur_unit,
            'ttb': exchange_rate.ttb,
            'tts': exchange_rate.tts,
            'deal_bas_r': exchange_rate.deal_bas_r
        }
        return JsonResponse(data)
    except Exchange.DoesNotExist:
        return JsonResponse({'error': 'Exchange rate not found'}, status=404)
