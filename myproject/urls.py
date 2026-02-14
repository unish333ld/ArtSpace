from django.contrib import admin
from django.urls import path

from main.views import index, logout_view, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('logout/', logout_view, name='logout'),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
]
