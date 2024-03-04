# example/views.py
from django.http import HttpResponse
import json
#import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    
    if request.method == 'POST':
        response = JsonResponse({'key': 'POST'})    
        #print(request["usuario"])
        return HttpResponse(response, content_type="application/json")
    
  
    response = JsonResponse({'key': 'GET'}) 
 
    return HttpResponse(response, content_type="application/json")

   