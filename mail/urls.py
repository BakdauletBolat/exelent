from .views import index
from django.urls import path

urlpatterns = [
    path('<int:pk>/',index,name="mailsend")
]
