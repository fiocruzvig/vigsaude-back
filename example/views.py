# example/views.py
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from example.exceptions.Exceptions import require_post
from  example.LoginFormRequest.loginFormRequest import LoginFormRequest
from example.services.login_service import LoginService

import json



@csrf_exempt
@require_post
@require_http_methods(["POST"])
def login(request):
        data = json.loads(request.body)
        form = LoginFormRequest(data)

        
        if not form.is_valid():
           errors = dict(form.errors.items())
           return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Erros de Validação', 'errors': errors}),  content_type="application/json", status= 400) 

        
        if LoginService().auth(data["username"], data["password"]) is None:
                return HttpResponse(JsonResponse({'status': 'Acesso Negado', 'message':'Usuário Inexistente'}), content_type="application/json", status=403)
        
        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso'}), content_type="application/json", status=200)

    
  

   