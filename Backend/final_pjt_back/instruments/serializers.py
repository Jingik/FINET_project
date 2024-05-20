from rest_framework import serializers
from .models import *

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'

class DepositProductsSerializer(serializers.ModelSerializer):
    deposit_options = DepositOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'

class SavingProductsSerializer(serializers.ModelSerializer):
    saving_options = SavingOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = SavingProducts
        fields = '__all__'

class CreditLoanOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditLoanOptions
        fields = '__all__'

class CreditLoanProductsSerializer(serializers.ModelSerializer):
    creditloan_options = CreditLoanOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = CreditLoanProducts
        fields = '__all__'
