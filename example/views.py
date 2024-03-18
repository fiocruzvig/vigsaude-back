# example/views.py
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from example.exceptions.Exceptions import require_post
import json


@csrf_exempt
@require_post
@require_http_methods(["POST"])
def login(request):   
        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso'}), content_type="application/json", status=200)

    
  

   