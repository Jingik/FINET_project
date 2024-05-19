from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Exchange
from .serializers import ExchangeSerializer
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

EXCHANGE_API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={settings.EXCHANGE_API_KEY}&searchdate=20240516&data=AP01'

@api_view(['GET'])
def index(request):
    response = requests.get(EXCHANGE_API_URL).json()
    if response:
        for item in response:
            cur_unit = item['cur_unit']
            Exchange.objects.update_or_create(
                cur_unit=cur_unit,
                defaults={
                    'cur_nm': item['cur_nm'],
                    'ttb': item['ttb'],
                    'tts': item['tts'],
                    'deal_bas_r': item['deal_bas_r']
                }
            )

    exchange_response = Exchange.objects.all()
    serializer = ExchangeSerializer(exchange_response, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def exchange_rate_detail(request, cur_unit):
    exchange_rate = get_object_or_404(Exchange, cur_unit=cur_unit)
    serializer = ExchangeSerializer(exchange_rate)
    return Response(serializer.data)