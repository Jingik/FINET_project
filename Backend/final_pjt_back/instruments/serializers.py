from rest_framework import serializers
from .models import *

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'
        
class DepositOptionsSerializer(serializers.ModelSerializer):
    class DepositSerializer(serializers.ModelSerializer):
        class Meta:
            model = DepositProducts
            fields = '__all__'
    deposit = DepositSerializer()
    
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('deposit',)
        
        
class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'
        
class SavingOptionSerializer(serializers.ModelSerializer):
    class SavingSerializer(serializers.ModelSerializer):
        class Meta:
            model = SavingProducts
            fields = '__all__'
            
    saving = SavingSerializer()
    
    class Meta:
        model = SavingOptions
        fields = '__all__'