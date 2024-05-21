from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Product, UserProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'interest_rate']

class UserProductSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = UserProduct
        fields = ['id', 'user', 'product', 'product_id', 'subscribed_at']
        
class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'id', 'username', 'password', 'password_confirm', 'name', 
            'phone_number', 'email', 'user_age_group', 'service_purpose', 
            'asset'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        subscribed_products = validated_data.pop('subscribed_products', [])
        validated_data.pop('password_confirm')
        validated_data['password'] = make_password(validated_data['password'])
        user = super(UserSerializer, self).create(validated_data)
        for product in subscribed_products:
            UserProduct.objects.create(user=user, product=product)
        return user

    def update(self, instance, validated_data):
        subscribed_products = validated_data.pop('subscribed_products', None)
        instance = super(UserSerializer, self).update(instance, validated_data)
        if subscribed_products is not None:
            instance.subscribed_products.set(subscribed_products)
        return instance
