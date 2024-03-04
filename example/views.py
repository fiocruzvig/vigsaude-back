# example/views.py
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')  
        body = json.loads(body_unicode)       
        response = JsonResponse(body)

        return HttpResponse(response, content_type="application/json")
    
  
    response = JsonResponse({'key': 'GET'}) 
 
    return HttpResponse(response, content_type="application/json")

   