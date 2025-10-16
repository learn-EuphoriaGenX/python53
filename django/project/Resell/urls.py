
from django.contrib import admin
from django.urls import path, include
from .views import Home, About, Contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home, name="home"),
    path("about/", About, name="about"),
    path("contact/", Contact, name="contact"),
    path("accounts/", include('accounts.urls'), name="accounts"),
    path("commerce/", include('commerce.urls'), name="commerce"),

]
