from .models import Exchange
from rest_framework import serializers

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ['cur_unit','ttb','tts','deal_bas_r',]