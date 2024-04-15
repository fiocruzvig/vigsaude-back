from django.http import HttpResponse
from django.http import JsonResponse
import json
from  example.LoginFormRequest.loginFormRequest import LoginFormRequest


def require_post(function):
    def wrapped_view(request, *args, **kwargs):
        
        if request.method != 'POST':
            return HttpResponse(JsonResponse({'status':'Erro', 'message': 'Método HTTP Inválido'}), content_type="application/json", status=405)
        
        elif not request.body:
            return HttpResponse(JsonResponse({'status': 'Erro','message':'Requisição sem Corpo'}), content_type="application/json", status=400)
        
        return function(request, *args, **kwargs)
    return wrapped_view


