# example/views.py
from django.http import HttpResponse
import json

def index(request):
    data = {'key': 'valor'}
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type="application/json")