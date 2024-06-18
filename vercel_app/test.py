import os
from django.conf import settings

from dotenv import load_dotenv
from .base import *
load_dotenv() 

SECRET_KEY = os.getenv('API_KEY')
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
MONGO_DATABASE = {
      'DRIVER': os.getenv('DRIVER_MONGO'),
      'USER': os.getenv('USER_MONGO'),
      'PASSWORD':os.getenv('PASSWORD_MONGO'),
      'HOST':os.getenv('HOST_MONGO'),
      'PORT':' '
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