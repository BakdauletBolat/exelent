from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render

from mail.models import TypeSeminar, Mail
from .forms import MailForm
from django.core.mail import send_mail
from django.http import HttpResponse

from django.contrib import messages


# Create your views here.


def success(request, pk):
    seminar = TypeSeminar.objects.get(id=pk)
    context = {
        'seminar': seminar
    }
    return render(request, 'mail/success_page.html', context);


def index(request, pk):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = 'Уважаемый ' + cd['name']

            # mail = send_mail(name, content, 'excellent@mail.kz', [cd['email'],'gulnaz_808@mail.ru','excellent.kaz@bk.ru','bakosh21345@gmail.com'])
            # if mail:
            obj = form.save()
            obj.typeSeminar_id = pk
            obj.save()
            typeSeminar = get_object_or_404(TypeSeminar, id=pk)
            messages.success(request,
                             f'{name}! Благодарим Вас за регистрацию! {typeSeminar.name}')
            return redirect(reverse('success_page', args=[pk]))
            # else:
            # messages.error(request, 'Ошибка при отправление письмо')
            # return redirect('mailsend')
        else:
            messages.error(request, 'Вы ввели неправильные данные')
            print(form)
            return redirect(reverse('success_page', args=[pk]))

    else:
        form = MailForm()

        typeSeminar = get_object_or_404(TypeSeminar, id=pk)
        context = {
            'form': form,
            'typeSeminar': typeSeminar
        }

        return render(request, 'mail/send.html', context)
