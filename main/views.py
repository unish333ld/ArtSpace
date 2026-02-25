from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.template.defaulttags import comment

from main.form import RegisterForm, MasterClassCreateForm
from main.models import MasterClass, ProfileUser


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = form.save()

            fio = request.POST['fio']
            phone = request.POST['phone']

            profile = ProfileUser()
            profile.user = user
            profile.phone = phone
            profile.fio = fio
            profile.save()

            login(request, user)
            return redirect("cabinet_user")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect('index')


def cabinet_user(request):
    master_class_list = MasterClass.objects.filter(user=request.user).order_by("-pk")
    context = {"list": master_class_list, 'page_name': "Страница просмотра мастер-классов"}
    return render(request, "list.html", context)


def admin_view(request):
    master_class_list = MasterClass.objects.order_by("-pk")
    context = {"list": master_class_list, 'page_name': "Кабинет администратора"}
    return render(request, "list.html", context)


def create_order(request):
    if request.method == "POST":
        form = MasterClassCreateForm(request.POST)
        if form.is_valid():
            masterclass = form.save(commit=False)
            masterclass.user = request.user
            masterclass.save()
            return redirect("cabinet_user")
    else:
        form = MasterClassCreateForm(request.GET or None)

    context = {'form': form}
    return render(request, "create_order.html", context)


def change_status(request, master_id, status_id):
    masterclass = get_object_or_404(MasterClass, pk=master_id)
    masterclass.status = status_id
    masterclass.save()
    return redirect('admin_view')


def cancel_order(request, master_id):
    masterclass = get_object_or_404(MasterClass, pk=master_id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        masterclass.status = 5
        masterclass.comment = comment
        masterclass.save()
        return redirect('admin_view')

    context = {'masterclass': masterclass}
    return render(request, "cancel_order.html", context)
