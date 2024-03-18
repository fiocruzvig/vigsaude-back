from django.http import HttpResponse
from django.http import JsonResponse
import json
from example.errors.errors import ApiErrors
from ..LoginFormRequest.loginFormRequest import LoginFormRequest


def require_post(function):
    def wrapped_view(request, *args, **kwargs):
        
        if request.method != 'POST':
            return HttpResponse(JsonResponse({'status':'Erro', 'message': 'Método HTTP Inválido'}), content_type="application/json", status=405)
        
        elif not request.body:
            return HttpResponse(JsonResponse({'status': 'Erro','message':'Requisição sem Corpo'}), content_type="application/json", status=400)
        
        else:
            data = json.loads(request.body)
            form = LoginFormRequest(data)
        
            if not form.is_valid():
                errors = dict(form.errors.items())
                return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Erros de Validação', 'errors': errors}),  content_type="application/json", status= 400)
                
        return function(request, *args, **kwargs)
    return wrapped_view


