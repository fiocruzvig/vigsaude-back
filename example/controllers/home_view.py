from django.http import HttpResponse
import os
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
import pandas as pd
import warnings
from example.services.create_csv_file import CreateCSVFILE

from example.services.mongo_pool import MongoPool
from example.services.mongo_service import MongoService
from vercel_app import dev
import json

class HomeView(APIView):
      
      #permission_classes = [IsAuthenticated]

       
      def get(self, request):
          return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso'}), content_type="application/json", status=200)

      def post(self, request):
          warnings.filterwarnings('ignore', category=UserWarning)
          mongo_pool = MongoPool()

          if 'xls_file' not in request.FILES:
               return HttpResponse(JsonResponse({'status': 'Erro', 'message':'O Ficheiro apresentou problemas'}), content_type="application/json", status=500)
          
          if not mongo_pool.connect():
               return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Falha na Conexão com o MongoDB'}), content_type="application/json", status=500)

          
          file = request.FILES['xls_file']
          
          db = mongo_pool.get_db()
       
          collection = mongo_pool.get_collection(db)
          mongo_service = MongoService()
          mongo_service.insert(file, collection)
        
          
         
          headers = pd.read_excel(file, header=None).iloc[0].to_dict()
          return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso', 'headers': headers}), content_type="application/json", status=200)

       


