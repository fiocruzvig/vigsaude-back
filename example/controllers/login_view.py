from django.http import HttpResponse
import json
from django.http import JsonResponse
from example.dtos.response.user_response import UserResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from  example.dtos.request.loginFormRequest import LoginFormRequest
from example.services.login_service import LoginService


import json




class LoginView(APIView):
      

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
        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso','Refresh':str(refresh),'Token':str(refresh.access_token)}), content_type="application/json", status=200)

