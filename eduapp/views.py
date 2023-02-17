from django.shortcuts import render

from feedback.models import Feedback
from mail.models import TypeSeminar
from .models import Page, Slider


def registerSeminarPage(request):
    typeSeminars = TypeSeminar.objects.filter(is_active=True)

    context = {
        'typeSeminars': typeSeminars
    }
    return render(request, 'eduapp/page/registerSeminar.html', context)


def main(request):
    slides = Slider.objects.all()
    pages = Page.objects.all().order_by('-created_at')
    feedbacks = Feedback.objects.all().order_by('-created_at').filter(is_confirmed=True)[:4]
    data = {
        'feedbacks': feedbacks,
        'slides': slides,
        'pages': pages
    }
    return render(request, 'eduapp/index.html', data)


def aboutUs(request):
    return render(request, 'eduapp/about-us.html')


def accelerationProgramm(request):
    return render(request, 'eduapp/programacceleration.html')


def direction(request):
    return render(request, 'eduapp/direction.html')


def training(request):
    return render(request, 'eduapp/training.html')


def contact(request):
    return render(request, 'eduapp/contact.html')


def page_detail(request, pk):
    page = Page.objects.get(id=pk)
    data = {
        'page': page
    }
    return render(request, 'eduapp/page/page_detail.html', data)
