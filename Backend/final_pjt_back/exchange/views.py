from django.conf import settings
from rest_framework.response import Response
from .models import Exchange
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from .serializers import ExchangeSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


# EXCHANGE_API_KEY = 'BDEnNlZa0E5gjifaBugXl6cHON5XSFnZ' # 환율 인증 키
EXCHANGE_API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={settings.EXCHANGE_API_KEY}&data=AP01'

@api_view(['GET'])
def index (request):
    response = requests.get(EXCHANGE_API_URL).json()
    exchange_response = Exchange.objects.all()

    if response: # 가 있다면기존 데이터를 업데이트
        if not exchange_response: # 쿼리셋이 비어있다면
                serializer = ExchangeSerializer(data=response, many=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
        else: # exchange_response 존재한다면
            Exchange.objects.all().delete()
            serializer = ExchangeSerializer(data=response, many=True)     
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    # 없다면
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