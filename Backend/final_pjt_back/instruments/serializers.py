from rest_framework import serializers
from .models import *
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'phone_number', 'email', 'user_age_group', 'service_purpose', 'asset']

## Deposit

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'

class DepositProductsSerializer(serializers.ModelSerializer):
    deposit_options = DepositOptionsSerializer(many=True, read_only=True, source='depositoptions_set')

    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositSubscription
        fields = '__all__'

class FavoriteDepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteDepositProduct
        fields = '__all__'


## Saving

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'

class SavingProductsSerializer(serializers.ModelSerializer):
    saving_options = SavingOptionsSerializer(many=True, read_only=True, source='savingoptions_set')
    
    class Meta:
        model = SavingProducts
        fields = '__all__'


class SavingSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingSubscription
        fields = '__all__'

class FavoriteSavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteSavingProduct
        fields = '__all__'
        
        
## Creditloan

class CreditLoanOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditLoanOptions
        fields = '__all__'

class CreditLoanProductsSerializer(serializers.ModelSerializer):
    creditloan_options = CreditLoanOptionsSerializer(many=True, read_only=True, source='creditloanoptions_set')

    class Meta:
        model = CreditLoanProducts
        fields = '__all__'

class CreditLoanSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditLoanSubscription
        fields = '__all__'

class FavoriteCreditLoanProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCreditLoanProduct
        fields = '__all__'