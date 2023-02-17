from django import forms

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    full_name = forms.CharField(
        required=True,
        label="ФИО",
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6 mb-4',
            'placeholder': 'ФИО',
            'required': True
        })
    )

    email = forms.EmailField(
        required=True,
        label="Почта",
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6 mb-4',
            'type': 'email',
            'placeholder': 'Почта',
            'required': True
        })
    )

    text = forms.CharField(
        required=True,
        label="Отзыв",
        widget=forms.Textarea(attrs={
            'class': 'form-control col-6 mb-4',
            'placeholder': 'Отзыв',
            'required': True
        })
    )

    class Meta:
        model = Feedback
        fields = ('email', 'full_name', 'text')
