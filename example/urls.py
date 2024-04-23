# example/urls.py
from django.urls import path

from example.controllers.login_view import LoginView 
from example.controllers.logout_view import LogoutView 


urlpatterns = [
    path('api/login',LoginView.as_view(), name='login'),
    path('api/logout',LogoutView.as_view(), name='logout'),
]