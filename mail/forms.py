from django import forms
from django.forms import fields, models
from .models import Mail


class MailForm(forms.ModelForm):
    name = forms.CharField(
        label="Пишите свою имя",

        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
            'placeholder': 'Пишите имя'
        })
    )
    lastname = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
        })
    )

    surname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
        })
    )

    universityjob = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
        })
    )

    consent = forms.Field(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-control-input',
        })
    )

    email = forms.EmailField(
        required=True,
        label="Пишите свою почту)",
        widget=forms.EmailInput(attrs={
            'class': 'form-control col-6',
            'required': True
        })
    )
    phone = forms.CharField(
        label="Пишите свой номер",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
            'placeholder': '8 (777) 777 77 77 ',
        })
    )

    class Meta:
        model = Mail
        fields = '__all__'
