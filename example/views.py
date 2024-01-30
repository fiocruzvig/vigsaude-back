# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    
    return HttpResponse("Sejam bem-vindos!")