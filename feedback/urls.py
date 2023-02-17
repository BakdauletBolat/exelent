from django.urls import path

from .views import create_feedback, success_feedback, FeedbackListView

urlpatterns = [
    path('create/', create_feedback, name='create-feedback'),
    path('list/', FeedbackListView.as_view(), name='list-feedback'),
    path('success/', success_feedback, name='success-feedback')
]
