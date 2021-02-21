from django.shortcuts import redirect, render
from .forms import MailForm
from django.core.mail import send_mail
from django.http import HttpResponse

from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            name = 'Уважемый '+cd['name']  
            message = cd['content']   
            mail = send_mail(name, message, 'excellent@mail.kz', [cd['email']])   
            if mail:
                form.save()
                messages.success(request, 'Ваше письмо успешно отправлено спасибо за ваш отклик'+name)
                return redirect('index')    
            else:
                messages.error(request, 'Ошибка при отправление письмо')
        else:
            messages.error(request, 'Вы ввели неправильные данные')
            
    else:       
        form = MailForm()

        context = {
            'form':form
        }
        return render(request, 'mail/send.html',context)