from django.http import HttpResponse
from django.http import JsonResponse
import json



'''


class LoginFormRequest:
        def __init__(self, request):
                self.usuario = request["usuario"]
                self.senha = request["senha"]

        def is_valid(self,):
                return len(self.usuario) == 5 and len(self.senha) == 5
'''

def require_post(function):
    def wrapped_view(request, *args, **kwargs):
        if request.method != 'POST':
            return HttpResponse(JsonResponse({"Status":"Método Inválido"}), content_type="application/json", status=405)
        
        '''
        
        body_unicode = request.body.decode('utf-8')  
        body = json.loads(body_unicode) 
        login_form = LoginFormRequest(body)
        
        if not login_form.is_valid():
                return HttpResponse(JsonResponse({"Status":"Dados Inválidos"}), content_type="application/json", status=401)  
        '''
        return function(request, *args, **kwargs)
    return wrapped_view

