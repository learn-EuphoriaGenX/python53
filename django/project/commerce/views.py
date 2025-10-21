from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required( login_url='login' )
def Shop(request):
    return render(request, 'shop.html')

@login_required( login_url='login' )
def Add_Category(request):
    if not request.user.is_superuser:
        return  redirect('restrict')
    return render(request, 'add_category.html')

@login_required( login_url='login' )
def Add_Product(request):
    if not request.user.is_superuser:
        return  redirect('restrict')
    return render(request, 'add_product.html')
