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
            name = 'Уважаемый '+cd['name']
            content = """
               Благодарим Вас за регистрацию! Ссылка на участие в семинаре будет направлена Вам на электронную почту в день проведения семинара.
            """
            mail = send_mail(name, content, 'excellent@mail.kz', [cd['email'],'gulnaz_808@mail.ru','excellent.kaz@bk.ru','bakosh21345@gmail.com'])
            if mail:
                form.save()
                messages.success(request, f'{name}! Благодарим Вас за регистрацию! Ссылка на участие в семинаре будет направлена Вам на электронную почту в день проведения семинара.')
                return redirect('mailsend')
            else:
                messages.error(request, 'Ошибка при отправление письмо')
                return redirect('mailsend')
        else:
            messages.error(request, 'Вы ввели неправильные данные')
            return redirect('mailsend')

    else:       
        form = MailForm()

        context = {
            'form':form
        }
        return render(request, 'mail/send.html',context)