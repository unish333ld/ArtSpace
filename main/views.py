from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from main.models import MasterClass


def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def logout_view(request):
    logout(request)
    return redirect('index')

def  cabinet_user(request):
    master_class_list = MasterClass.objects.filter(user=request.user).order_by("-pk")
    context = {"master_class_list": master_class_list}
    return render(request, "list.html", context)

def admin_view(request):
    master_class_list = MasterClass.objects.order_by("-pk")
    context = {"master_class_list": master_class_list}
    return render(request, "list.html", context)