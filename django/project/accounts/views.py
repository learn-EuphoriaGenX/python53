from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        if username and password:
            user = User.objects.filter(username=username).exists()
            if user:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful.')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid password.')
                    return redirect('login')
            else:
                messages.error(request, 'Username does not exist.')
                return redirect('login')                
        else:
            messages.error(request, 'Both fields are required.')
            return redirect('login')

    return render(request, 'login.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return redirect('register')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'All fields are required.')
            return redirect('register')
 
    return render(request, 'register.html')

def Logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')
