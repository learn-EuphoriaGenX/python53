from django.urls import path
from .views import  Login, Register, Logout, Admin_Restricted, User_profile

urlpatterns = [
    path("login/", Login, name="login"),
    path("register/", Register, name="register"),
    path("logout/", Logout, name="logout"),
    path("admin-restricted/", Admin_Restricted, name="restrict"),
    path("profile/", User_profile, name="profile"),
]
