from tkinter.font import names

from django.contrib.auth.models import User
from django.db import models


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name  # или другое поле с названием


class Tema(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='temas')

    def __str__(self):
        return self.name


class MasterClass(models.Model):
    FORMAT_CHOICES = {
        1: "Очная встреча",
        2: "Онлайн",
    }
    METHODS_PAYMENT_CHOICES = {
        1: "Банковская плата",
        2: "Онлайн-перевод",
    }
    STATUS_CHOICES = {
        1: "Черновик",
        2: "На модерации",
        3: "Опубликован",
        4: "Идёт проведение",
        5: "Завершён",
        6: "Отклонён",
    }
    name = models.CharField(max_length=200, verbose_name='Название мастер-класса')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, verbose_name='Тема')
    description = models.CharField(max_length=200, verbose_name='Краткое описание')
    count = models.IntegerField(verbose_name='Количество доступных мест для записи')
    date_event = models.DateField(verbose_name='Дата проведения')
    duration = models.CharField(max_length=200, verbose_name='Продолжительность занятие')
    format = models.IntegerField(choices=FORMAT_CHOICES, verbose_name='Формат')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость участия')
    method_payment = models.IntegerField(choices=METHODS_PAYMENT_CHOICES, verbose_name='Способы оплаты')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    comment = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
