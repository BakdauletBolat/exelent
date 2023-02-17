from .views import index, success
from django.urls import path

urlpatterns = [
    path('<int:pk>/', index, name="mailsend"),
    path('success/<int:pk>/', success, name="success_page")
]
