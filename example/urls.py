# example/urls.py
from django.urls import path

from example.views import login


urlpatterns = [
    path('', login),
]