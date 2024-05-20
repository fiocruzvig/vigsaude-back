# example/urls.py
from django.urls import path, include, re_path
from example.controllers.login_view import LoginView 
from example.controllers.logout_view import LogoutView 
from example.controllers.home_view import HomeView


urlpatterns = [
    path('api/login',LoginView.as_view(), name='login'),
    path('api/logout',LogoutView.as_view(), name='logout'),
    path('api/home',HomeView.as_view(), name='home'),
    #re_path(r'^upload/(?P<filename>[^/]+)$', HomeView.as_view())

]