from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from main.models import MasterClass, Tema


class RegisterForm(UserCreationForm):
    fio = forms.CharField(label='ФИО', max_length=100)
    phone = forms.CharField(label='Your phone', max_length=100)

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

        # Только POST, нахуй GET
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