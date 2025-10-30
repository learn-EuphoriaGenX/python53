from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Product, Cart, Order

# Create your views here.
@login_required( login_url='login' )
def Shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    if 'cat' in request.GET:
        category_id = request.GET['cat']
        if Category.objects.filter(id=category_id).exists():
            category = Category.objects.get(id=category_id)
            products = products.filter(category=category)
        else:
            messages.error(request, 'Selected category does not exist.')
            return redirect('shop')

    if 'type' in request.GET:
        product_type = request.GET['type']
        if product_type in ['Male', 'Female', 'Unisex']:
            products = products.filter(gender=product_type)  
        elif product_type == 'all':
            pass
        else:
            messages.error(request, 'Invalid product type selected.')
            return redirect('shop') 
        
    if 'sort' in request.GET:
        sort_option = request.GET['sort']
        if sort_option == 'low':
            products = products.order_by('discounted_price')
        elif sort_option == 'high':
            products = products.order_by('-discounted_price')
        elif sort_option == 'featured':
            products = products.filter(is_featured=True)
        else:
            messages.error(request, 'Invalid sorting option selected.')
            return redirect('shop')

    data = { 'categories': categories, 'products': products }
    return render(request, 'shop.html', data)

@login_required( login_url='login' )
def Add_Category(request): 
    if not request.user.is_superuser:
        return  redirect('restrict')
    
    if request.method == 'POST':
        category_name = request.POST.get('categoryName')
        category_image = request.FILES.get('categoryImage')

        if not category_name or not category_image:
            messages.error(request, 'Both category name and image are required.')
            return redirect('add_category')

        # Create and save the new category
        new_category = Category(name=category_name, image=category_image)
        new_category.save()
        messages.success(request, 'Category added successfully.')

        return redirect('add_category')

    return render(request, 'add_category.html')

@login_required( login_url='login' )
def Add_Product(request):
    if not request.user.is_superuser:
        return  redirect('restrict')
    
    categories = Category.objects.all()
    data = {'categories': categories}

    if request.method == 'POST':
        product_name = request.POST.get('productName')
        category_id = request.POST.get('category')
        original_price = request.POST.get('originalPrice')
        discounted_price = request.POST.get('discountedPrice')
        product_image = request.FILES.get('productImage')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        is_featured = request.POST.get('isFeatured') == 'on'

        if not product_image or not product_name or not category_id or not original_price or not discounted_price or not description or not stock:
            messages.error(request, 'All fields are required.')
            return redirect('add_product')
        
        new_product = Product(
            name=product_name,
            category=Category.objects.get(id=category_id),
            original_price=original_price,
            discounted_price=discounted_price,
            image=product_image,
            description=description,
            stock=stock,
            is_featured=is_featured
        )
        new_product.save()
        messages.success(request, 'Product added successfully.')
        return redirect('add_product')

    return render(request, 'add_product.html', data)
