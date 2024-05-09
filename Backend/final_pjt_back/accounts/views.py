from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

#임시

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
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if username and password:
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                return JsonResponse({'message': 'Signup successful'})
        else:
            return JsonResponse({'error': 'Username and password are required'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['GET'])
def user_profile(request, username):
    if request.method == 'GET':
        user = User.objects.filter(username=username).first()
        if user:
            user_profile = {
                'username': user.username,
                'email': user.email,
                # Add more profile information as needed
            }
            return JsonResponse({'user_profile': user_profile})
        else:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
