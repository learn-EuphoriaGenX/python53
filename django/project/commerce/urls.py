from django.urls import path, include
from .views import Shop, Add_Category, Add_Product

urlpatterns = [
    path("shop/", Shop, name="shop"),
    path("add-category/", Add_Category, name="add_category"),
    path("add-product/", Add_Product, name="add_product"),
]
