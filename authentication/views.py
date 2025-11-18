from django.contrib.auth.models import User
import json

from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from django.contrib.auth import logout as auth_logout


# Create your views here.
logger = logging.getLogger(__name__)



@csrf_exempt
def logout(request):
    username = request.user.username
    try:
        auth_logout(request)
        logger.info(f"User {username} logged out successfully.")
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logged out successfully!"
        }, status=200)
    except:
        logger.error(f"Logout failed for user {username}.")
        return JsonResponse({
            "status": False,
            "message": "Logout failed."
        }, status=401)
        
        
@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Login status successful.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login successful!"
                # Add other data if you want to send data to Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account is disabled."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, please check your username or password."
        }, status=401)
        
        
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']

        # Check if the passwords match
        if password1 != password2:
            logger.warning(f"Password mismatch for username: {username}")
            return JsonResponse({
                "status": False,
                "message": "Passwords do not match."
            }, status=400)
            
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            logger.warning(f"Attempt to register with existing username: {username}")
            return JsonResponse({
                "status": False,
                "message": "Username already exists."
            }, status=400)
            
        
        # Create the new user
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        
        return JsonResponse({
            "username": user.username,
            "status": 'success',
            "message": "User created successfully!"
        }, status=200)
    
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)