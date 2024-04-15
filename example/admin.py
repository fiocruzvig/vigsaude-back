from django.contrib import admin
from django.contrib.auth import authenticate


class User:
    def __init__(self, ):
        pass
    
    def auth(self, username, password):
        return  authenticate(username=username, password=password)


