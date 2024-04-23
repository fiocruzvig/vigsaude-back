from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView



class LogoutView(APIView):
     permission_classes = [IsAuthenticated]
     def delete(self, request):
          return HttpResponse(JsonResponse({'status': 'OK', 'message': 'sucesso'}), content_type='application/json', status=200)


   