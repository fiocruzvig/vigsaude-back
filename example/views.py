# example/views.py
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from example.exceptions.Exceptions import require_post
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.views import APIView
from  example.LoginFormRequest.loginFormRequest import LoginFormRequest
from example.services.login_service import LoginService

import json




class LoginView(APIView):
      
      permission_classes = [IsAuthenticated]

      def post(self, request):
        data = json.loads(request.body)
        form = LoginFormRequest(data) 

        if not form.is_valid():
           errors = dict(form.errors.items())
           return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Erros de Validação', 'errors': errors}),  content_type="application/json", status= 400) 

        user = LoginService().auth(data["username"], data["password"])
        if user is None:
                return HttpResponse(JsonResponse({'status': 'Acesso Negado', 'message':'Usuário Inexistente'}), content_type="application/json", status=403)
        
        refresh = RefreshToken.for_user(user)
        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso', 'Refresh':str(refresh),'Token':str(refresh.access_token)}), content_type="application/json", status=200)


'''
permission_classe = [IsAuthenticated]
@csrf_exempt
@require_post
@require_http_methods(["POST"])
def login(request):
        data = json.loads(request.body)
        form = LoginFormRequest(data)

        
        if not form.is_valid():
           errors = dict(form.errors.items())
           return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Erros de Validação', 'errors': errors}),  content_type="application/json", status= 400) 

        user = LoginService().auth(data["username"], data["password"])
        if user is None:
                return HttpResponse(JsonResponse({'status': 'Acesso Negado', 'message':'Usuário Inexistente'}), content_type="application/json", status=403)
        
        refresh = RefreshToken.for_user(user)
        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso', 'Refresh':str(refresh),'Token':str(refresh.access_token)}), content_type="application/json", status=200)

'''
  

   