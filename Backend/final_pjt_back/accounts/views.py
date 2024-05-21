from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.contrib.auth import login
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import *
from django.contrib.auth.hashers import check_password
from .models import *
from rest_framework.authtoken.models import Token
import traceback
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET'])
def id_check_exists(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        if username:
            user_exists = User.objects.filter(username=username).exists()
            return JsonResponse({'exists': user_exists})
        else:
            return JsonResponse({'error': 'Username parameter is missing'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['POST'])
def signup(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'message': 'Signup successful', 'token': token.key}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(traceback.format_exc())  # 예외 발생 시 전체 스택 트레이스를 출력합니다.
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def user_login(request):
    """
    사용자 로그인
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return JsonResponse({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    if check_password(password, user.password):
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'message': 'Login successful', 'token': token.key}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def user_profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_profile = {
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'phone_number': user.phone_number,
            'user_age_group': user.user_age_group,
            'service_purpose': user.service_purpose,
            'asset': user.asset,
        }
        return JsonResponse({'user_profile': user_profile}, status=status.HTTP_200_OK)

    if request.method in ['PUT', 'PATCH']:
        serializer = UserSerializer(user, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe_product(request):
    user = request.user
    product_id = request.data.get('product_id')

    if not product_id:
        return Response({'detail': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    user_product, created = UserProduct.objects.get_or_create(user=user, product=product)

    if not created:
        return Response({'detail': 'Already subscribed'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserProductSerializer(user_product)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_subscriptions(request):
    user = request.user
    subscriptions = UserProduct.objects.filter(user=user)
    serializer = UserProductSerializer(subscriptions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)