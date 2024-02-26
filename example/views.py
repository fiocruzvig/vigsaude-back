# example/views.py
from django.http import HttpResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    print(request)
    if request.method == 'POST':
        data = {'key': 'POST'}
        print("Aqui")
        response_data = json.dumps(data)
        return HttpResponse(response_data, content_type="application/json")
    return HttpResponse("Olá")

    # data = {'key': 'GET'}
    #r = requests.get('https://jsonplaceholder.typicode.com/users')
    #print(r)
    #usuarios = r.json()
    #print(requests)
    # response_data = json.dumps(data)
    # return HttpResponse(response_data, content_type="application/json")