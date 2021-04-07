from .views import main,aboutUs,direction,training,contact,accelerationProgramm
from django.urls import path,include

urlpatterns = [
    path('',main,name="index"),
    path('mail',include('mail.urls')),
    path('accelereationprogramm/',accelerationProgramm,name="aprogram"),
    path('about-us/',aboutUs,name="aboutUs"),
    path('direction/',direction,name="direction"),
    path('training/',training,name="training"),
    path('contact/',contact,name="contact")
]
