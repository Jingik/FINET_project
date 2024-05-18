from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.contrib.auth import login
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.hashers import check_password
from .models import User
from rest_framework.authtoken.models import Token

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
    username = request.data.get('username')
    password = request.data.get('password')
    password2 = request.data.get('password2')

    if not username or not password or not password2:
        return JsonResponse({'error': 'Username, password, and password confirmation are required'}, status=status.HTTP_400_BAD_REQUEST)

    if password != password2:
        return JsonResponse({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    token, created = Token.objects.get_or_create(user=user)
    return JsonResponse({'message': 'Signup successful', 'token': token.key}, status=status.HTTP_201_CREATED)


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