# example/urls.py
from django.urls import path

from example.views import LoginView


urlpatterns = [
    path('api/login',LoginView.as_view(), name='login'),
]