from django.http import HttpResponse
from django.http import JsonResponse
import json
from ..LoginFormRequest.loginFormRequest import LoginFormRequest



def require_post(function):
    def wrapped_view(request, *args, **kwargs):
        if request.method != 'POST':
            return HttpResponse(JsonResponse({"Status":"Método Inválido"}), content_type="application/json", status=405)
        
        body_unicode = request.body.decode('utf-8')  
        body = json.loads(body_unicode) 

        login_form = LoginFormRequest(body)
        patterns = login_form.patterns
        for key in patterns:
            if not login_form .is_valid(patterns[key], key):
                return HttpResponse(JsonResponse({"Status":"Dados Inválidos"}), content_type="application/json", status=401)  
        return function(request, *args, **kwargs)
    return wrapped_view

