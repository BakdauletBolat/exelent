from django import forms
from django.forms import fields, models
from .models import Mail

class MailForm(forms.ModelForm):

    surname = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
        })
    )
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
        })
    )
    universityjob = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
        })
    )
    position = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
        })
    )
    consent = forms.Field(
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-control-input',
        })
    )
    name = forms.CharField(
        label = "Пишите свою имя",
        widget=forms.TextInput(attrs={
            'class':'form-control col-6',
            'placeholder':'Пишите ФИО'
        })
    )

    email = forms.EmailField(
        label = "Пишите свою почту)",
        widget=forms.EmailInput(attrs={
            'class':'form-control col-6',
            'placeholder':'arman@example.com'
        })
    )

    phone = forms.CharField(
        label = "Пишите свой номер",
        widget=forms.TextInput(attrs={
            'class':'form-control col-6',
            'placeholder':'8 (777) 777 77 77 ',
        })
    )
    class Meta:
        
        model = Mail
        fields = ('__all__')