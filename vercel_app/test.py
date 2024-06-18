import os

from dotenv import load_dotenv
from .base import *
load_dotenv() 

SECRET_KEY = os.getenv('API_KEY')
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']




MONGO_DATABASE = {
      'DRIVER': os.getenv("MONGO_DRIVER"),
      'USER': os.getenv('MONGO_USER'),
      'PASSWORD':os.getenv('MONGO_PASSWORD'),
      'HOST':os.getenv('MONGO_HOST'),
      'PORT':os.getenv('MONGO_PORT')
}


DATABASES = {
        'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('NAME_PG'),
        'USER':os.getenv('USER_PG'),
        'PASSWORD':os.getenv('PASSWORD_PG'),
        'HOST':os.getenv('HOST_PG'),
        'PORT':os.getenv('PORT_PG')
    }
  
}