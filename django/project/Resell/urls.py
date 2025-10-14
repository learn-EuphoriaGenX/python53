
from django.contrib import admin
from django.urls import path
from .view import Home, Login, Register, About, Shop, Contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home, name="home"),
    path("login/", Login, name="login"),
    path("register/", Register, name="register"),
    path("about/", About, name="about"),
    path("shop/", Shop, name="shop"),
    path("contact/", Contact, name="contact"),

]
