from django import forms
from django.forms import fields, models
from .models import Mail

class MailForm(forms.ModelForm):

    name = forms.CharField(
        label = "Пишите свою имя",
        widget=forms.TextInput(attrs={
            'class':'form-control col-6',
            'placeholder':'Пишите имя'
        })
    )
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
        })
    )

    surname = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
        })
    )
    
    universityjob = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
        })
    )
    # position = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control col-6',
    #     })
    # )
    consent = forms.Field(
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-control-input',
        })
    )
  

    email = forms.EmailField(
        label = "Пишите свою почту)",
        widget=forms.EmailInput(attrs={
            'class':'form-control col-6',
            'placeholder':'arman@example.com',
            'required':True,
            'pattern': "/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/"
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