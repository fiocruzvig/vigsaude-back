import re
from django.core import validators
from django import forms


class LoginFormRequest(forms.Form):
    username = forms.CharField(min_length=1)
    email = forms.EmailField()
    password = forms.CharField(min_length=8)    
