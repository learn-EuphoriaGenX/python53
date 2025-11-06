from django.db import models
from django.contrib.auth.models import User

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return f'{self.name} Category'
    
# product model
class Product(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unisex', 'Unisex'),
    ]

    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    gender = models.CharField(max_length=50, choices=gender_choices, default='Unisex')
    description = models.TextField()
    stock = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} Product'
    
# Cart model
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Cart Item: {self.product.name} for {self.user.username}'

# Order model 
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)
    payment_method = models.CharField(default='COD', max_length=50)

    def __str__(self):
        return f'Order: {self.product.name} by {self.user.username}'
    
