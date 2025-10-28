from django.shortcuts import render
from commerce.models import Category, Product

def Home(request):
    categoies = Category.objects.all()[:4]
    prducts = Product.objects.filter(is_featured=True)[:4]
    data = { 'categories': categoies, 'products': prducts }
    return render(request, 'home.html', data)

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')