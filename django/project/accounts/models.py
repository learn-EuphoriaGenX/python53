from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=gender_choices, blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
    
class Address (models.Model):
    type_choices = [
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    postal_code = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='India')
    type = models.CharField(max_length=50, choices=type_choices, default='Home')

    def __str__(self):
        return f'Address for {self.user.username}'