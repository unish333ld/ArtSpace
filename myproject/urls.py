from django.contrib import admin
from django.urls import path

from main.views import index, logout_view, register, cabinet_user, admin_view, create_order, change_status, cancel_order
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('logout/', logout_view, name='logout'),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
    path('admin_panel/', admin_view, name='admin_view'),
    path('cabinet/', cabinet_user, name='cabinet_user'),
    path('create_order/', create_order, name='create_order'),
    path("masterclass/<int:master_id>/status/<int:status_id>/", change_status, name="change_status"),
    path("masterclass/<int:master_id>/", cancel_order, name="cancel_order"),
]
