from .views import main,aboutUs,direction,training,contact
from django.urls import path

urlpatterns = [
    path('',main,name="index"),
    path('about-us/',aboutUs,name="aboutUs"),
    path('direction/',direction,name="direction"),
    path('training/',training,name="training"),
    path('contact/',contact,name="contact")
]
