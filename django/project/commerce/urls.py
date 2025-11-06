from django.urls import path, include
from .views import Shop, Add_Category, Add_Product, Product_details, My_cart, Add_cart, Remove_item, Update_cart

urlpatterns = [
    path("shop/", Shop, name="shop"),
    path("add-category/", Add_Category, name="add_category"),
    path("add-product/", Add_Product, name="add_product"),
    path("<int:id>",Product_details , name="details"),
    path("cart/",My_cart , name="cart"),
    path("add-cart/<int:id>/",Add_cart , name="add-cart"),
    path("remove-item/<int:id>/",Remove_item , name="remove_item"),
    path("update-cart/<int:id>/",Update_cart , name="update_cart"),
]
