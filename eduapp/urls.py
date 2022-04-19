from .views import main,aboutUs,direction,training,contact,accelerationProgramm, page_detail,registerSeminarPage
from django.urls import path,include

urlpatterns = [
    path('', main, name="index"),
    path('register-seminar/',registerSeminarPage,name='register-seminar'),
    path('mail', include('mail.urls')),
    path('accelereationprogramm/', accelerationProgramm, name="aprogram"),
    path('about-us/', aboutUs, name="aboutUs"),
    path('direction/', direction, name="direction"),
    path('training/', training, name="training"),
    path('contact/', contact, name="contact"),
    path('p/<int:pk>/', page_detail, name="page_detail")
]
