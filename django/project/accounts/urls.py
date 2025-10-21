from django.urls import path
from .views import  Login, Register, Logout, Admin_Restricted

urlpatterns = [
    path("login/", Login, name="login"),
    path("register/", Register, name="register"),
    path("logout/", Logout, name="logout"),
    path("admin-restricted/", Admin_Restricted, name="restrict"),
]
