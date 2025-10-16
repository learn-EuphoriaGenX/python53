from django.urls import path, include
from .views import Shop

urlpatterns = [
    path("shop/", Shop, name="shop"),
]
