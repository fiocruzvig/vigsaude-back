# example/views.py
from django.http import HttpResponse
import json
import requests

def index(request):
    data = {'key': 'valor'}
    #r = requests.get('https://jsonplaceholder.typicode.com/users')
    #print(r)
    #usuarios = r.json()
    #print(requests)
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type="application/json")