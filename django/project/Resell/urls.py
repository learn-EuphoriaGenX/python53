
from django.contrib import admin
from django.urls import path, include
from .views import Home, About, Contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", Home, name="home"),
    path("about/", About, name="about"),
    path("contact/", Contact, name="contact"),
    path("accounts/", include('accounts.urls'), name="accounts"),
    path("commerce/", include('commerce.urls'), name="commerce"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
