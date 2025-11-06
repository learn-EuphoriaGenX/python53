from django.shortcuts import render
from commerce.models import Category, Product, Cart

def Home(request):
    categoies = Category.objects.all()[:4]
    prducts = Product.objects.filter(is_featured=True)[:4]
    data = { 'categories': categoies, 'products': prducts }
    cart_items_count = 0
    # SAVE CART ITEMS COUNT IN COOKIES
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
        data['cart_items_count'] = cart_items_count

    return render(request, 'home.html', data)

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')