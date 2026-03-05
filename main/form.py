from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator

from main.models import MasterClass, Tema

class RegisterForm(UserCreationForm):

    username = forms.CharField(
        label='Логин',
        max_length=150,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9]{6,}$',
                message='Логин должен содержать только латинские буквы и цифры и быть не менее 6 символов'
            )
        ]
    )

    fio = forms.CharField(
        label='ФИО',
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[А-Яа-яЁё\s]+$',
                message='ФИО должно содержать только буквы кириллицы и пробелы'
            )
        ]
    )

    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^8\(\d{3}\)\d{3}-\d{2}-\d{2}$',
                message='Телефон должен быть в формате 8(XXX)XXX-XX-XX'
            )
        ]
    )

    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "fio", "phone", "email"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})
        self.fields["fio"].widget.attrs.update({"class": "form-control"})
        self.fields["phone"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})


class MasterClassCreateForm(ModelForm):
    class Meta:
        model = MasterClass
        exclude = ["status", "comment", "user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
        self.fields["date_event"].widget.attrs.update({"placeholder": "ДД.ММ.ГГГГ"})

        # Только POST
        if self.data and 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['tema'].queryset = Tema.objects.filter(category_id=category_id)
            except:
                self.fields['tema'].queryset = Tema.objects.none()
        elif self.instance.pk:
            self.fields['tema'].queryset = self.instance.category.temas.all()
        else:
            self.fields['tema'].queryset = Tema.objects.none()