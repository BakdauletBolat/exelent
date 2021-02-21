from django import forms
from django.forms import fields, models
from .models import Mail

class MailForm(forms.ModelForm):
    
    name = forms.CharField(
        label = "Пишите свою имя)",
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Пишите ФИО'
        })
    )

    email = forms.EmailField(
        label = "Пишите свою почту)",
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'arman@example.com'
        })
    )

    content = forms.Field(
        label = "Пишите текст вашего сообщений",
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'placeholder':''
        })
    )
    class Meta:
        
        model = Mail
        fields = ('__all__')