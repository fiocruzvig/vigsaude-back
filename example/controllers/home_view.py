from django.http import HttpResponse
import os
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
import pandas as pd
import warnings
from example.services.create_csv_file import CreateCSVFILE



class HomeView(APIView):
      
      permission_classes = [IsAuthenticated]

      def get(self, request):
          return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso'}), content_type="application/json", status=200)

      def post(self, request):
          warnings.filterwarnings('ignore', category=UserWarning)
          
          if 'xls_file' not in request.FILES:
               return HttpResponse(JsonResponse({'status': 'Erro', 'message':'O Ficheiro apresentou problemas'}), content_type="application/json", status=500)
          
          
          file = request.FILES['xls_file']
          csf = CreateCSVFILE(file)
          csf.create_buffer_csv()
          csf.create_path("./ficheiros")      
       
         
          headers = pd.read_excel(file, header=None).iloc[1].to_dict()
          return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso', 'headers': headers}), content_type="application/json", status=200)

       


