from django.shortcuts import render

# Create your views here.

def main(request):

    return render(request,'eduapp/index.html')

def aboutUs(request):

    return render(request,'eduapp/about-us.html')

def accelerationProgramm(request):

    return render(request,'eduapp/programacceleration.html')

def direction(request):

    return render(request,'eduapp/direction.html')

def training(request):

    return render(request,'eduapp/training.html')

def contact(request):

    return render(request,'eduapp/contact.html')