from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Address
# Create your views here.
def Login(request):

    if request.user.is_authenticated:
        return redirect('home')

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
    if request.user.is_authenticated:
        return redirect('home')
    
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
    if not request.user.is_authenticated:
        return redirect('home')
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

def Admin_Restricted(request):
    return render(request, 'admin-restricted.html')

@login_required( login_url='login' )
def User_profile(request):
    user = request.user

    profile, created = Profile.objects.get_or_create(user=request.user)
    addresses = Address.objects.filter(user=user).order_by('-id')

    if request.method == 'POST':
        # ---------------------- Profile Update ----------------------
        if 'profile-update' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            gender = request.POST.get('gender')
            avatar = request.FILES.get('avatar')

            user.username = username
            user.email = email
            user.save()

            if avatar:
                profile.avatar = avatar
            profile.phone = phone
            profile.gender = gender
            profile.save()

            messages.success(request, 'Profile updated successfully.')

        if 'add-address' in request.POST:
            full_name = request.POST.get('full_name')
            phone = request.POST.get('address_phone')
            postal_code = request.POST.get('pincode')
            address_text = request.POST.get('address_line')
            city = request.POST.get('city')
            state = request.POST.get('state')
            address_type = request.POST.get('address_type')

            new_address = Address(
                user=user,
                full_name=full_name,
                phone=phone,
                postal_code=postal_code,
                address=address_text,
                city=city,
                state=state,
                type=address_type
            )
            new_address.save()
            messages.success(request, 'Address added successfully.')

    data = {
        'profile': profile,
        'addresses': addresses
    }
    
    return render(request, 'profile.html', data)